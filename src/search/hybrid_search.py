from src.search.keywordSearcher import KeywordSearcher
from src.search.semantic_search import SemanticSearcher


class HybridSearcher:
    def __init__(self, k: int = 60):
        self.semantic_searcher = SemanticSearcher()
        # pull the real archive chunks once, to build the keyword index
        all_chunks = self.semantic_searcher.get_all_chunks()
        self.keyword_searcher = KeywordSearcher(all_chunks)
        self.k = k

    def search(self, query: str, top_k: int = 5) -> list:
        keyword_results = self.keyword_searcher.search(query, top_k=10)
        semantic_results = self.semantic_searcher.search(query, top_k=10)

        rrf_scores = {}
        chunk_lookup = {}

        for rank, chunk in enumerate(keyword_results):
            chunk_id = chunk["id"]
            rrf_scores[chunk_id] = rrf_scores.get(chunk_id, 0) + 1 / (self.k + rank + 1)
            chunk_lookup[chunk_id] = chunk

        for rank, chunk in enumerate(semantic_results):
            chunk_id = chunk["id"]
            rrf_scores[chunk_id] = rrf_scores.get(chunk_id, 0) + 1 / (self.k + rank + 1)
            chunk_lookup.setdefault(chunk_id, chunk)  # don't overwrite a richer keyword-side chunk

        sorted_ids = sorted(rrf_scores.keys(), key=lambda cid: rrf_scores[cid], reverse=True)

        results = []
        for chunk_id in sorted_ids[:top_k]:
            chunk = chunk_lookup[chunk_id]
            results.append({**chunk, "rrf_score": rrf_scores[chunk_id]})
        return results


if __name__ == "__main__":
    searcher = HybridSearcher()
    results = searcher.search("who ruled after a war over powerful artifacts")
    for r in results:
        print(r["id"], "-", round(r["rrf_score"], 4), "-", r.get("source", "?"), "-", r["text"][:60])