import re
from rank_bm25 import BM25Okapi
from src.search.sample_data import SAMPLE_CHUNKS


class KeywordSearcher:
    def __init__(self, chunks: list):
        self.chunks = chunks
        self.tokenized_corpus = [self._tokenize(c["text"]) for c in chunks]
        self.bm25 = BM25Okapi(self.tokenized_corpus)

    def _tokenize(self, text: str) -> list:
        return re.findall(r"\b\w+\b", text.lower())

    def search(self, query: str, top_k: int = 10) -> list:
        tokenized_query = self._tokenize(query)
        scores = self.bm25.get_scores(tokenized_query)

        scored_chunks = list(zip(self.chunks, scores))
        scored_chunks.sort(key=lambda pair: pair[1], reverse=True)

        results = []
        for chunk, score in scored_chunks[:top_k]:
            results.append({**chunk, "keyword_score": float(score)})
        return results


if __name__ == "__main__":
    searcher = KeywordSearcher(SAMPLE_CHUNKS)
    results = searcher.search("Ashvael", top_k=5)
    for r in results:
        print(r["id"], "-", round(r["keyword_score"], 2), "-", r["text"][:60])