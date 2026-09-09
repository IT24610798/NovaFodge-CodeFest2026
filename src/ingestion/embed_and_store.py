"""
embed_and_store.py — turns chunks into "fingerprints" (embeddings) and
files them in the card catalog (ChromaDB).

Setup before running:
  1. pip install -r requirements.txt
  2. Get a free Voyage AI API key: https://www.voyageai.com/
  3. Put it in your .env file as VOYAGE_API_KEY=your-key-here
"""

import os
import voyageai
import chromadb
from tqdm import tqdm

VOYAGE_MODEL = "voyage-2"  # good default free-tier embedding model
CHROMA_PATH = "./data/chroma_db"  # persists to disk, survives restarts
COLLECTION_NAME = "kingdom_archive"
BATCH_SIZE = 16  # embed in small batches so one API hiccup doesn't lose all your work


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


def embed_and_store_chunks(chunks, log_file="ingestion_failures.log"):
    """
    chunks: list of dicts as produced by chunker.chunk_records()
    Embeds them in batches and upserts into Chroma.
    Failures are logged, not silently swallowed — this feeds limitations.md.
    """
    voyage = get_voyage_client()
    collection = get_chroma_collection()

    failures = []

    for i in tqdm(range(0, len(chunks), BATCH_SIZE), desc="Embedding + storing"):
        batch = chunks[i:i + BATCH_SIZE]
        texts = [c["text"] for c in batch]

        try:
            result = voyage.embed(texts, model=VOYAGE_MODEL, input_type="document")
            embeddings = result.embeddings
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
        print(f"⚠️  {len(failures)} chunks failed to embed. See {log_file}")

    print(f"✅ Stored {collection.count()} total chunks in '{COLLECTION_NAME}'")
    return collection


def quick_search_test(query, n_results=3):
    """Sanity check: does search return anything sensible at all?
    Run this after your first ingestion pass, before building anything else."""
    voyage = get_voyage_client()
    collection = get_chroma_collection()

    query_embedding = voyage.embed([query], model=VOYAGE_MODEL, input_type="query").embeddings[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)

    for doc, meta, dist in zip(
        results["documents"][0], results["metadatas"][0], results["distances"][0]
    ):
        print(f"\n--- distance={dist:.3f} | source={meta['source']} | reliability={meta['reliability']} ---")
        print(doc[:200], "...")


if __name__ == "__main__":
    # Quick manual test — run: python ingestion/embed_and_store.py
    quick_search_test("What happens if the Dragon King's sword breaks?")