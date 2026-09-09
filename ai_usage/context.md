# Shared Context for AI Tools

This is the background/context our team gave repeatedly to Claude while building this
project. We're including it so judges can see what information the AI tool was working
from, and evaluate our prompting approach. All four members used Claude for their part, so
this same context block was the starting point across all four sets of sessions.

## Competition
SLIIT Codefest 2026 AI Competition (powered by IFS). Sub-track **1C — Searching the Way a
Human Does** (agentic/iterative search). Team of 4, working inside the 28 August – 9
September 2026 initial-round window. Deadline: 9 September 2026, 11:30 PM.

## The corpus
"The Ashen Era Archive" — a fictional fantasy franchise archive built specifically for this
competition, so general model knowledge is useless; the system must work from the provided
files only. 415 documents, ~1,277 pages, mixed formats (PDF, DOCX, Markdown, plain text,
simulated scans):
- `chronicles/` — 4 novel volumes (long narrative)
- `wiki/` — ~90 fan-wiki style articles
- `codex/` — official lore data books with tables/figure plates
- `ephemera/` — ~150 in-world letters, ledgers, trial transcripts (scanned pages included) —
  explicitly **unreliable narrators by design**
- `images/` — standalone figure plates

Facts about characters/factions/events are scattered and sometimes **contradict** across
these folders on purpose — that's the core difficulty of the challenge. A correct system
should surface contradictions with attribution rather than silently picking one source.

## What we're building
An agentic search system: search → reflect ("do I have enough to answer?") → search again
with a reformulated query if not → stop and answer with cited evidence, capped at a small
number of iterations (configurable in the UI, default 3).

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
  real decisions (see `docs/decisions.md`, and the resume-after-failure fix documented
  under Person 1 in `ai-usage-disclosure.md`).
- Everything must run from a clean clone using only the README.
- Every AI conversation must be exported and disclosed — no exceptions, no penalty for
  disclosing, real risk in hiding.
- The corpus intentionally contains contradictions across `ephemera/` (unreliable) vs
  `codex/`/`chronicles/` (more authoritative) — any AI-suggested logic that resolves or
  hides a contradiction instead of surfacing it with a reliability tag should be treated as
  a bug, not a feature.
- Sub-track priority for testing: 1C questions (our own track) first, then 1B (multi-hop,
  a good stress test for the same search loop), then 1A (image/figure-plate questions) only
  if time allows — 1A questions about portraits and plates often can't be answered from
  text alone, since those images produce no extractable text on ingestion, which is a
  corpus-coverage limitation rather than a search-agent failure.