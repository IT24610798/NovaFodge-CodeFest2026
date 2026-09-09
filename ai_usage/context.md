# Shared Context for AI Tools

This is the background/context our team gave repeatedly to AI assistants (ChatGPT, Claude,
Copilot, etc.) while building this project. We're including it so judges can see what
information the AI tools were working from, and evaluate our prompting approach.

## Competition
SLIIT Codefest 2026 AI Competition (powered by IFS). Sub-track **1C — Searching the Way a
Human Does** (agentic/iterative search). Team of 4, 5-day build inside a 2-week window.
Deadline: 9 September 2026, 11:30 PM.

## The corpus
"The Ashen Era Archive" — a fictional fantasy franchise archive built specifically for this
competition, so general model knowledge is useless; the system must work from the provided
files only. 415 documents, ~1,277 pages, mixed formats (PDF, DOCX, Markdown, plain text,
simulated scans):
- `chronicles/` — novel volumes (long narrative)
- `wiki/` — ~90 fan-wiki style articles
- `codex/` — official lore data books with tables/figure plates
- `ephemera/` — ~150 in-world letters, ledgers, trial transcripts (scanned pages included) —
  explicitly **unreliable narrators by design**
- `images/` — standalone figure plates

Facts about characters/factions/events are scattered and sometimes **contradict** across these
folders on purpose — that's the core difficulty of the challenge.

## What we're building
An agentic search system: search → reflect ("do I have enough to answer?") → search again with
a reformulated query if not → stop and answer with cited evidence, capped at ~5 iterations.

Stack: Python, Voyage AI (embeddings), ChromaDB (vector store), OpenRouter free-tier models
(LLM), Streamlit (demo UI).

## Team roles
- **Person 1** — document parsing, chunking, embedding pipeline (ingestion → ChromaDB)
- **Person 2** — the search/reflect/search agent loop + LLM connection
- **Person 3** — Streamlit UI, including a visible reasoning trace
- **Person 4** (me) — testing, documentation, AI-usage disclosure and log organization

## Constraints we keep repeating to AI tools
- Free-tier APIs only where possible; Voyage AI free tier without a card is capped at
  **3 requests/minute**, which makes embedding the full corpus slow — this shaped several
  real decisions (see `docs/decisions.md`).
- Everything must run from a clean clone using only the README.
- Every AI conversation must be exported and disclosed — no exceptions, no penalty for
  disclosing, real risk in hiding.