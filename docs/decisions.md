# Architecture and Engineering Decisions

This document records the decisions that shaped the archive question-answering system and the
reasoning behind them.

## 1. Use a hybrid retriever

We combine BM25 keyword search with Voyage semantic search and merge the ranked results using
reciprocal rank fusion. Keyword search preserves exact names, dates, and artifact terms, while
semantic search handles paraphrased questions. Combining both is more reliable for the archive
than depending on either method alone.

## 2. Persist embeddings in ChromaDB

Embeddings are stored in a persistent ChromaDB database at `data/chroma_db` in the
`kingdom_archive` collection. This avoids rebuilding the index whenever the application starts
and lets the search layer use the same data produced by ingestion.

## 3. Use deterministic chunk IDs

Chunk IDs are an MD5 hash of the source filename, page number, and chunk index. Earlier runs
used random IDs, which made resume-after-failure impossible because the same chunk received a
different ID on every run. Deterministic IDs allow ingestion to skip chunks already stored in
ChromaDB after a rate-limit interruption.

## 4. Chunk documents with overlap

Documents are split into 800-character chunks with 100 characters of overlap. The overlap helps
preserve context across chunk boundaries while keeping embedding requests small enough for the
available API limits.

## 5. Prioritize text collections under API limits

Because the Voyage AI free tier limits embedding requests, we prioritized `codex/`, `wiki/`,
and `chronicles/` before adding a small `ephemera/` sample. This gives the main search flow
coverage of the highest-value text sources while documenting the remaining corpus gap instead
of silently presenting incomplete coverage as complete.

## 6. Keep raw ingestion evidence

Ingestion failures and skipped files are appended to `docs/limitations.md` rather than deleted
or rewritten. The raw log provides evidence for image, OCR, PDF, and rate-limit limitations and
allows future runs to be compared with earlier runs.

## 7. Use an agentic search loop with a bounded budget

The agent searches, asks the reflection model whether the evidence is sufficient, and optionally
reformulates the query before searching again. The default maximum is three iterations. A bound
keeps API usage and response time predictable, while the limitation is documented for questions
that require more chained lookups.

## 8. Keep answer generation grounded in retrieved context

The final-answer prompt instructs the LLM to use only retrieved chunks and to state what is
missing when the context is insufficient. This reduces unsupported claims, while the remaining
need for explicit contradiction resolution is documented in `docs/limitations.md`.