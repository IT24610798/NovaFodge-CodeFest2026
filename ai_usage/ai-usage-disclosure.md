# AI Usage Disclosure

**Team name:** Novafodge
**Sub-track:** 1C — Searching the Way a Human Does
**Date:** 2026-09-09
**Competition:** SLIIT Codefest 2026 (powered by IFS)

Per the competition's AI Usage Policy: honest disclosure of every tool used carries no
penalty. Omitting a tool that was actually used is a misrepresentation risk. This document
is the plain-English summary; the full raw conversation exports live alongside it in
`ai_usage/` (see "Where the raw logs are," below) — judges can cross-check this summary
against them.

## 1. Tools used — summary table

| Tool | Used by | Purpose |
|---|---|---|
| Claude (Anthropic) | Person 1 | Document parsing/chunking/embedding pipeline (ingestion → ChromaDB) |
| Claude (Anthropic) | Person 2 | Search/reflect/search agent loop + LLM connection |
| Claude (Anthropic) | Person 3 | Streamlit UI, including the visible reasoning trace |
| Claude (Anthropic) | Person 4 | Rules/rubric comprehension, documentation, AI-usage disclosure, testing |

All four members used Claude for their respective parts of the build. If any teammate also
used a second tool (ChatGPT, Copilot, Cursor, etc.) at any point, add a row for it — leaving
it out when it was actually used is the one thing that risks a penalty here.

---

## 2. Person 1 — Ingestion Pipeline

**Role:** Document parsing, chunking, embedding pipeline (ingestion → ChromaDB)
**Tool used:** Claude (Anthropic)
**What the AI did:** Helped build the ingestion pipeline end-to-end — parsers for PDF (with
OCR fallback), DOCX, TXT, MD, and images; chunking logic; reliability-tier tagging; Voyage AI
embedding calls into ChromaDB; environment setup for Tesseract and Poppler; and debugging of
real errors hit during testing.

**Where we steered the AI / overrode its first suggestion:**
- The corpus README defines folder-based reliability categories ("official," "fan-wiki,"
  "narrative," "unreliable in-world authors"). Claude's first suggestion merged the `wiki/`
  folder into the "official" tier. We pushed back and corrected this to a separate
  "reference" tier, since the README specifically distinguishes fan-written wiki content
  from official codex records — treating them the same would have erased a distinction the
  corpus was designed to test.
- Some documents exist as both `.docx` and `.pdf` with identical content in the
  `chronicles`/`codex` folders. Claude's first suggestion was a blanket rule: always prefer
  `.docx` and drop the `.pdf` duplicate, applied corpus-wide. Before applying it everywhere,
  we manually checked a same-named pair in `ephemera/` and found they were **completely
  different documents** that only coincidentally shared a filename. We restricted the
  dedup rule to `chronicles`/`codex` (manually verified identical pairs) and explicitly
  excluded `ephemera/` — an unchecked AI-suggested rule would have silently deleted real,
  unique corpus content.
- Resume-after-failure logic (to avoid re-embedding already-stored chunks after hitting
  Voyage AI's free-tier rate limit) never actually worked, because chunk IDs were generated
  with `uuid.uuid4()` on every run, so no two runs ever produced matching IDs. We diagnosed
  this ourselves by comparing a real "already stored" ID against a real "freshly generated"
  ID side by side, confirmed the mismatch, and fixed it by switching to deterministic
  hash-based IDs (filename + page + chunk index) so re-runs correctly resume.
- Hit `TesseractNotFoundError` and `PDFInfoNotInstalledError` on Windows (both tools
  installed but not on PATH). Pasted the real tracebacks to Claude, got a fix (setting tool
  paths explicitly in code), and verified it with a direct sanity check
  (`pytesseract.get_tesseract_version()`) before moving on.
- 54 files failed to parse with "produced no text." We did not accept Claude's first framing
  of these as failures — manually checked the file list, confirmed they were all pure
  illustration images (concept art with no printed text, correctly identified by OCR as
  having nothing to extract), and reclassified them in code and in `limitations.md` as an
  intentional skip rather than a parsing failure.
- Hit Voyage AI's free-tier rate limit (3 requests/minute without a payment method) partway
  through the real embedding run. Rather than accepting partial, undocumented coverage, we
  added resume logic and retry-with-backoff, then made an explicit, disclosed trade-off:
  fully embedded codex/wiki/chronicles, plus a verified sample from ephemera (confirmed
  present and retrievable via a direct metadata filter query), with full ephemera coverage
  logged as a known, time-boxed limitation rather than a silent gap.

**Why this matters for the grade:** every bullet above is a case of the team catching an
AI suggestion that would have been wrong for this specific corpus and correcting it with
evidence, not just accepting the first answer.

---

## 3. Person 2 — Agent Loop (search / reflect / search)

**Role:** Search → reflect → search agent loop + LLM connection (OpenRouter free-tier model)
**Tool used:** Claude (Anthropic)
**What the AI did:** Based on the actual code in the repo, Claude helped scaffold
`run_agentic_search()` in `agent_loop.py` (the search → reflect → reformulate-query loop,
capped at `max_iterations`), the `reflect()` function in `reflect.py` (prompts the LLM for a
strict `SUFFICIENT: yes/no` + `NEW_QUERY` decision and parses the response), and
`HybridSearcher` in `hybrid_search.py` combining semantic and keyword search.

**Where we steered the AI / overrode its first suggestion:** *[Person 2 to fill in — this
needs your own memory of the real conversation, not a generic statement. One concrete thing
worth checking and writing up honestly: `reflect.py`'s `parse_reflection()` currently has
two different lines computing `is_sufficient`, where the second silently overwrites the
first (the first line's result is never used). Was this a real bug you found while testing
and patched — and if so, what did you see that made you realize it, and how did you verify
the fix worked? If it was something else, replace this with your own real example. Other
prompts to jog memory:*
- *Did Claude suggest a stopping condition or iteration cap that didn't fit the free-tier
  rate limits, and you changed it?*
- *Did an early reflection prompt let the agent stop searching too early or loop too long
  on a real question, and you rewrote the prompt after seeing it fail?*
- *Did Claude suggest treating contradictory sources (e.g. `ephemera/` vs `codex/`) as an
  error to resolve, when the corpus intentionally wants both surfaced with attribution —
  and you corrected that?*
- *Did you paste a real error or a bad trace back to Claude and get a fix you then verified
  yourself?]*

**Status:** Placeholder — replace the bracketed section above with your own real example
before submission. Leaving this thin costs real marks under the 15%-weighted "team steered
the AI" criterion, and generic/invented claims here carry real disqualification risk if
they don't match your actual chat logs.

---

## 4. Person 3 — Streamlit UI

**Role:** Streamlit demo UI, including a visible reasoning trace
**Tool used:** Claude (Anthropic)
**What the AI did:** Based on the actual code in the repo, Claude helped scaffold the
Streamlit layout in `app.py` and `theme.py` — including the "Show search steps" toggle and
the "Max search iterations" slider visible in the sidebar, and the chat-style question input.

**Where we steered the AI / overrode its first suggestion:** *[Person 3 to fill in — needs
your own real example, not a generic statement. Prompts to jog memory:*
- *Did Claude's first UI draft hide or collapse the reasoning trace by default, when the
  whole point of sub-track 1C is showing the human-like search process — and you changed
  it to show it by default (the toggle in your current UI defaults to on — was that a
  deliberate correction, or the AI's first suggestion)?*
- *Did a first citation-rendering approach show snippets without a clear source/reliability
  tag, and you added tier labels (official / reference / narrative / unreliable) after
  reviewing it against the corpus structure?*
- *Did you hit a real Streamlit state-management bug (e.g. reruns wiping the trace or the
  passcode/secrets error) and fix it with a specific correction rather than accepting a
  generic answer?]*

**Status:** Placeholder — replace the bracketed section above with your own real example
before submission, for the same reason as Person 2's section.

---

## 5. Person 4 — Documentation, Testing, Disclosure

**Role:** Testing, documentation, AI-usage disclosure and log organization
**Tool used:** Claude (Anthropic)
**What the AI did:** Helped understand the competition rules/rubric, organize documentation
(`docs/decisions.md`, `docs/limitations.md`, `docs/testing.md`), draft the structure of this
disclosure and the shared-context file, and design the testing log — including prioritizing
1C questions first (the team's own sub-track), then 1B, then 1A, and specifically flagging
that 1A questions about portraits/figure-plate images can't be answered from the current
corpus coverage since those images produce no extractable text — a corpus-coverage
limitation, not a search-agent failure, and the testing log was written to record that
distinction rather than mark those rows as a plain fail.

**Where we steered the AI / overrode its first suggestion:**
Early conversations with Claude stayed too abstract ("explain agentic RAG") without grounding
in the team's actual repo state, which wasted time. The fix was to stop asking for general
explanations and instead paste real project evidence — the actual `limitations.md` ingestion
log, the actual folder structure — and ask Claude to work from that specific evidence. This
produced concrete, usable outputs (a reorganized `limitations.md`, a seeded `decisions.md`,
a testing log ordered by what the team's own sub-track is actually judged on) instead of
generic advice.

**Team decision:** we kept the raw ingestion logs as an appendix rather than deleting them,
since they're real evidence of iterative debugging (see the resume-logic bug documented
under Person 1 above, in `docs/decisions.md`). Claude's first suggestion was to rewrite them
from scratch for readability; we rejected that in favor of preserving the logs as evidence
of the actual process.

---

## 6. Where the raw logs are

Full, unedited conversation exports as `.txt` files:
- `ai_usage/claude_logs/person1_ingestion/`
- `ai_usage/claude_logs/person2_agent_loop/`
- `ai_usage/claude_logs/person3_ui/`
- `ai_usage/claude_logs/person4_docs_testing/`

Name each file `YYYY-MM-DD_topic.txt` (e.g. `2026-09-09_documentation-and-limitations.txt`)
so judges can follow the story in order. See `docs/log-organization-guide.md` for export
steps. *(If a second tool was used by anyone, add a matching `ai_usage/<tool>_logs/` folder
and a row in the summary table above — do not omit it.)*

## 7. Shared context given to AI tools

See `context.md` (in this same delivery) for the background/constraints repeated
across all four members' sessions with Claude.

---

This disclosure is mandatory per the competition's AI Usage Policy (Section 4.1). Honest
disclosure carries no penalty; omission or misrepresentation risks disqualification.