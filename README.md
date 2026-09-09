# NovaForge — Agentic Search over the Ashen Era Archive

SLIIT Codefest 2026 · Sub-track **1C: Searching the Way a Human Does**

An agentic search system that answers questions over a 415-document fantasy archive
(chronicles, wiki, codex, ephemera) where facts are deliberately scattered and sometimes
contradictory across sources. The agent searches, reflects on whether it has enough evidence,
reformulates its query and searches again if not, then answers with cited sources — instead of
grabbing the first match and stopping.

See `docs/architecture.md` for the full pipeline diagram, `docs/decisions.md` for why we chose
what we chose, and `docs/limitations.md` for what doesn't work yet and why.

## Stack

- **Ingestion:** Python, `pypdf`/`pytesseract` (OCR fallback for scanned pages), `python-docx`
- **Embeddings:** Voyage AI
- **Vector store:** ChromaDB
- **Search:** Hybrid — BM25 keyword search + semantic search, combined via Reciprocal Rank Fusion
- **LLM (reflection + answering):** OpenRouter free-tier models
- **UI:** Streamlit

## Setup

1. **Clone and enter the repo:**
   ```bash
   git clone https://github.com/IT24610798/NovaFodge-CodeFest2026.git
   cd NovaFodge-CodeFest2026
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up your API keys:**
   ```bash
   cp .env.example .env
   ```
   Open `.env` and fill in:
   - `VOYAGE_API_KEY` — from [voyageai.com](https://www.voyageai.com/)
   - `OPENROUTER_API_KEY` — from [openrouter.ai](https://openrouter.ai/)

4. **Install OCR dependencies (needed for scanned-page PDFs and standalone images):**
   - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
   - [Poppler](https://poppler.freedesktop.org/) (for PDF-to-image conversion)

   ⚠️ **Known setup gap:** `src/ingestion/loaders.py` currently has these tools' paths
   hardcoded for one teammate's Windows machine. On any other machine, either:
   - install both tools so they're on your system `PATH`, and remove/comment out the two
     hardcoded path lines near the top of `loaders.py`, **or**
   - edit those two lines to point at wherever Tesseract/Poppler are installed on your machine.

   *(We know this isn't ideal — see `docs/limitations.md`. Fixing it properly means reading
   these paths from environment variables instead; flagged for a future pass.)*

5. **Run ingestion** (parses the archive, chunks it, embeds it into ChromaDB):
   ```bash
   python src/ingestion/run_ingestion.py --input data/raw
   ```
   Use `--dry-run` to parse and chunk without embedding (useful for testing without burning
   API calls), and `--limit N` to only process the first N files.

6. **Run the demo:**
   ```bash
   streamlit run src/ui/app.py
   ```
   *(Update this path if the actual entry-point filename differs — Person 3 to confirm.)*

## Project structure

```
├── docs/            # architecture, decisions, limitations, testing notes
├── src/
│   ├── ingestion/   # document parsing, chunking, embedding
│   ├── search/      # the agentic search/reflect/search loop
│   ├── ui/          # Streamlit demo
│   └── utils/       # shared helpers
├── ai_usage/        # AI usage disclosure + chat log exports (see AI Usage Policy)
└── data/            # raw corpus + persisted ChromaDB (not committed — see .gitignore)
```

## AI usage disclosure

Full disclosure of every AI tool used while building this, including exported chat logs, is in
`ai_usage/ai-usage-disclosure.md`.

## Known limitations

See `docs/limitations.md` for a full, honest account — in short: ephemera document coverage is
partial (Voyage AI free-tier rate limits), and 54 illustration-only images have no extractable
text by design.