# AI Usage Disclosure

Per the competition's AI Usage Policy: honest disclosure of every tool used carries no penalty.
Omitting a tool that was actually used is a misrepresentation risk. This document is the
plain-English summary; the full raw conversation exports live alongside it in `ai_usage/`
(see "Where the raw logs are," below) — judges can cross-check this summary against them.

## Tools used by the team

| Tool | Used by | Purpose |
|---|---|---|
| Claude (Anthropic) | Person 4 | Understanding the competition rules/rubric, organizing documentation (`docs/decisions.md`, `docs/limitations.md`), drafting the AI-usage disclosure structure, testing methodology |
| [ChatGPT / other] | Person 4 | [Fill in — e.g. "Initial walkthrough of the ingestion pipeline and agent-loop concepts before code was reviewed"] |
| Claude (Anthropic) | Person 1 | Building the ingestion pipeline end-to-end: document parsers (PDF with OCR fallback, DOCX, TXT, MD, images), chunking logic, reliability-tier tagging, Voyage AI embedding + ChromaDB storage, environment setup (Tesseract, Poppler), and debugging real errors hit during testing |
| [Tool used by Person 2] | Person 2 | [Fill in — e.g. agent loop / reflection prompt design] |
| [Tool used by Person 3] | Person 3 | [Fill in — e.g. Streamlit UI scaffolding] |

*(Replace bracketed placeholders with what each person actually used — GitHub Copilot, Cursor,
ChatGPT, Claude, whatever it really was. Don't leave any teammate's row blank if they used
something.)*

## How we used AI — and where we overrode it

This is the part judges weight most heavily (15% of the grade): evidence that the team steered
the AI, not the other way around.

**Person 4 (documentation/testing) — example of real back-and-forth:**
Early on, conversations with an AI assistant stayed too abstract ("explain agentic RAG") without
grounding in the team's actual repo state, which wasted time. The fix was to stop asking for
general explanations and instead paste real project evidence (the actual `limitations.md`
ingestion log, the actual folder structure) and ask the AI to work from that specific evidence.
This produced concrete, usable outputs (a reorganized `limitations.md`, a seeded
`decisions.md`) instead of generic advice. **Team decision:** we chose to keep raw ingestion
logs as an appendix rather than delete them, since they're real evidence of iterative debugging
(see the resume-logic bug in `docs/decisions.md`) — the AI's first suggestion was to rewrite
them from scratch, which we rejected in favor of preserving them as evidence.

**Person 1 (ingestion) — examples of real back-and-forth and corrections:**
- The corpus README described folder-based reliability categories ("official," "fan-wiki,"
  "narrative," "unreliable in-world authors"). The AI's first suggestion merged the wiki folder
  into the "official" tier; this was pushed back on and corrected to a separate "reference" tier,
  since the README specifically distinguished fan-written wiki content from official codex
  records — treating them the same would have lost a real distinction the corpus was designed
  to test.
- Found that some documents existed as both `.docx` and `.pdf` with identical content
  (`chronicles`/`codex` folders) and initially applied a blanket rule to always prefer `.docx`
  and drop the `.pdf` duplicate. Before applying this corpus-wide, manually checked a same-named
  pair in the `ephemera` folder and discovered they were **completely different documents**
  that only coincidentally shared a filename. The deduplication rule was corrected to apply
  only to `chronicles`/`codex` (where pairs were manually verified identical), not `ephemera`
  — a blanket AI-suggested rule would have silently deleted real, unique corpus content.
- Hit a real bug where resume-after-failure logic (to avoid re-embedding already-stored chunks
  after hitting Voyage AI's free-tier rate limit) never worked, because chunk IDs were randomly
  generated (`uuid.uuid4()`) on every run, so no two runs ever produced matching IDs. Diagnosed
  this by comparing a real "already stored" ID against a real "freshly generated" ID side by
  side, confirmed the mismatch, and fixed it by switching to deterministic hash-based IDs
  (filename + page + chunk index) so re-runs correctly resume instead of restarting from zero.
- Encountered `TesseractNotFoundError` and `PDFInfoNotInstalledError` on Windows (Tesseract and
  Poppler installed but not on system PATH) — pasted the real tracebacks back to the AI, got a
  fix (setting the tool paths explicitly in code), and verified the fix worked with a direct
  sanity check (`pytesseract.get_tesseract_version()`) before moving on.
- When 54 files failed to parse with "produced no text," did not accept the AI's first framing
  of these as failures — manually checked the file list, confirmed they were all pure
  illustration images (concept art with no printed text, correctly identified by OCR as
  containing nothing to extract), and reclassified them in the code and in `limitations.md` as
  an intentional skip rather than a parsing failure.

**Person 2 / 3 — [fill in with real examples]:**
For each, note at least one moment where the team pushed back on or corrected an AI suggestion.
Example prompts to jog memory: "Did the AI suggest an approach we didn't use? Why not?" "Did we
paste an actual error back and ask why it happened?" "Did we ask 'why X over Y' and then decide
for ourselves?" If nothing comes to mind, that's a signal to have one more real conversation with
the AI tool today and note it here — thin evidence here costs real marks.

## Where the raw logs are

Full, unedited conversation exports as `.txt` files:
- `ai_usage/claude_logs/` — Claude conversations
- `ai_usage/chatgpt_logs/` — [rename/add folders per tool actually used]

Name each file `YYYY-MM-DD_topic.txt` (e.g. `2026-09-09_documentation-and-limitations.txt`) so
judges can follow the story in order. See `docs/log-organization-guide.md` for the export
steps.

## Shared context given to AI tools

See `ai_usage/context.md` for the background/constraints we repeated across sessions.
Team name: Diloosha Rajapaksha
Sub-track: 1C
Date: 2026.09.09

This disclosure is mandatory per the competition's AI Usage Policy (Section 4.1).
Honest disclosure carries no penalty; omission or misrepresentation risks
disqualification.

## 1. Tools used

## 2. What the AI did
## 3. What the team did

## 4. Chat logs

## 5. Team contributions