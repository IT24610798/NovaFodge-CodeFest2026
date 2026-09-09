import os
from dotenv import load_dotenv
import voyageai
import chromadb
from src.utils.retry import retry_on_rate_limit

load_dotenv()

VOYAGE_MODEL = "voyage-2"  # must match the model used during ingestion
CHROMA_PATH = "./data/chroma_db"  # same path Person 1's pipeline saves to
COLLECTION_NAME = "kingdom_archive"  # same collection name Person 1 used

voyage_client = voyageai.Client(api_key=os.environ["VOYAGE_API_KEY"])


class SemanticSearcher:
    def __init__(self):
        # PersistentClient reads the real saved database from disk,
        # instead of building a fresh empty one in memory each time
        chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
        self.collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)

    @retry_on_rate_limit(max_retries=5, base_delay=2.0)
    def search(self, query: str, top_k: int = 5) -> list:
        result = voyage_client.embed([query], model=VOYAGE_MODEL, input_type="query")
        query_embedding = result.embeddings[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        output = []
        for i in range(len(results["ids"][0])):
            chunk = {
                "id": results["ids"][0][i],
                "text": results["documents"][0][i],
                "semantic_score": results["distances"][0][i],
            }
            chunk.update(results["metadatas"][0][i] or {})  # adds source, doc_type, etc.
            output.append(chunk)
        return output

    def get_all_chunks(self) -> list:
        """Fetch every stored chunk - used to build the BM25 keyword index."""
        data = self.collection.get(include=["documents", "metadatas"])
        chunks = []
        for i in range(len(data["ids"])):
            chunk = {"id": data["ids"][i], "text": data["documents"][i]}
            chunk.update(data["metadatas"][i] or {})
            chunks.append(chunk)
        return chunks


if __name__ == "__main__":
    searcher = SemanticSearcher()
    print(f"Connected. Collection has {searcher.collection.count()} chunks.")
    results = searcher.search("who ruled after a war over powerful artifacts")
    for r in results:
        print(r["id"], "-", round(r["semantic_score"], 3), "-", r["text"][:60])