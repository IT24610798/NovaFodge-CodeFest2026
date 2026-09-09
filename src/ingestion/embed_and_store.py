import os
import time
import voyageai
import chromadb
from tqdm import tqdm

VOYAGE_MODEL = "voyage-2"  # good default free-tier embedding model
CHROMA_PATH = "./data/chroma_db"  # persists to disk, survives restarts
COLLECTION_NAME = "kingdom_archive"
BATCH_SIZE = 40  # kept moderate to stay under free-tier token limits per request


def get_voyage_client():
    api_key = os.environ.get("VOYAGE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "VOYAGE_API_KEY not set. Add it to your .env file."
        )
    return voyageai.Client(api_key=api_key)


def get_chroma_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    return client.get_or_create_collection(name=COLLECTION_NAME)


def embed_with_retry(voyage, texts, max_retries=5):
    """
    Wraps the Voyage embed call with exponential backoff. On the free
    tier without a payment method, Voyage enforces 3 requests/minute —
    this means a single rate-limit hit needs at least ~20s before
    retrying, not the classic 1-2-4-8s backoff, so we floor the wait
    at 20 seconds and let it grow from there for repeated failures.
    """
    for attempt in range(max_retries):
        try:
            result = voyage.embed(texts, model=VOYAGE_MODEL, input_type="document")
            return result.embeddings
        except Exception as e:
            wait = max(2 ** attempt, 20)
            print(f"Rate limited or error ({e}), retrying in {wait}s...")
            time.sleep(wait)
    raise RuntimeError("Failed after max retries")


def embed_and_store_chunks(chunks, log_file="ingestion_failures.log"):
    
    voyage = get_voyage_client()
    collection = get_chroma_collection()

    existing_ids = set(collection.get()["ids"])
    original_count = len(chunks)
    chunks = [c for c in chunks if c["id"] not in existing_ids]
    actually_skipped = original_count - len(chunks)
    print(f"Skipping {actually_skipped} already-stored chunks (out of {original_count} total).")
    print(f"{len(chunks)} chunks remaining to embed.")

    failures = []

    for i in tqdm(range(0, len(chunks), BATCH_SIZE), desc="Embedding + storing"):
        batch = chunks[i:i + BATCH_SIZE]
        texts = [c["text"] for c in batch]

        try:
            embeddings = embed_with_retry(voyage, texts)
        except Exception as e:
            for c in batch:
                failures.append(f"{c['metadata']['source']} (chunk {c['id']}): {e}")
            continue  # skip this batch, keep going — don't let one bad batch kill the run

        collection.upsert(
            ids=[c["id"] for c in batch],
            embeddings=embeddings,
            documents=texts,
            metadatas=[c["metadata"] for c in batch],
        )

    if failures:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write("\n".join(failures) + "\n")
        print(f"⚠️  {len(failures)} chunks failed to embed after retries. See {log_file}")

    print(f"✅ Stored {collection.count()} total chunks in '{COLLECTION_NAME}'")
    return collection


def quick_search_test(query, n_results=3):

    voyage = get_voyage_client()
    collection = get_chroma_collection()

    query_embedding = voyage.embed([query], model=VOYAGE_MODEL, input_type="query").embeddings[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)

    for doc, meta, dist in zip(
        results["documents"][0], results["metadatas"][0], results["distances"][0]
    ):
        print(f"\n--- distance={dist:.3f} | source={meta['source']} | reliability={meta['reliability_tier']} ---")
        print(doc[:200], "...")


if __name__ == "__main__":
    # Quick manual test
    quick_search_test("What happens if the Dragon King's sword breaks?")