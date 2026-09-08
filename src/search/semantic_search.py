import os
from dotenv import load_dotenv
import voyageai
import chromadb
from src.search.sample_data import SAMPLE_CHUNKS

load_dotenv()

voyage_client = voyageai.Client(api_key=os.environ["VOYAGE_API_KEY"])


class SemanticSearcher:
    def __init__(self, chunks: list = SAMPLE_CHUNKS):
        self.chunks = chunks

        # ChromaDB needs a "collection" - think of it like a table in a database
        chroma_client = chromadb.Client()
        self.collection = chroma_client.get_or_create_collection(name="ashen_era_archive")

        # Only build embeddings if the collection is empty (avoid redoing work)
        if self.collection.count() == 0:
            self._build_index()

    def _build_index(self):
        texts = [c["text"] for c in self.chunks]
        ids = [c["id"] for c in self.chunks]

        # Voyage AI turns each text into a list of numbers (an embedding)
        result = voyage_client.embed(texts, model="voyage-3", input_type="document")
        embeddings = result.embeddings

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
        )

    def search(self, query: str, top_k: int = 3) -> list:
        # embed the QUESTION the same way we embedded the documents
        result = voyage_client.embed([query], model="voyage-3", input_type="query")
        query_embedding = result.embeddings[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        output = []
        for i in range(len(results["ids"][0])):
            output.append({
                "id": results["ids"][0][i],
                "text": results["documents"][0][i],
                "semantic_score": results["distances"][0][i],
            })
        return output


if __name__ == "__main__":
    searcher = SemanticSearcher()
    results = searcher.search("who ruled after a war over powerful artifacts")
    for r in results:
        print(r["id"], "-", round(r["semantic_score"], 3), "-", r["text"][:60])