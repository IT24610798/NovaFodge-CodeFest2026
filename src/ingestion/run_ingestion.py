"""
run_ingestion.py — the one script that runs the whole pipeline.

Usage:
    python src/ingestion/run_ingestion.py --input data/raw --limit 5 --dry-run
    python src/ingestion/run_ingestion.py --input data/raw
"""

import argparse
import os
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

from loaders import load_document
from chunker import chunk_documents
from embed_and_store import embed_and_store_chunks

SUPPORTED_EXTS = {".pdf", ".docx", ".txt", ".md", ".jpg", ".jpeg", ".png"}


def collect_files(root_dir):
    """Walk the directory. source_type = the top-level folder name
    directly under root_dir (codex, wiki, chronicles, ephemera, images).
    Skips files sitting directly in root_dir (like README.txt).
    Only dedupes .docx/.pdf pairs in chronicles/codex, where they're
    confirmed identical content — NOT in ephemera, where matching
    filenames can be completely different documents (verified by hand)."""
    DEDUPE_FOLDERS = {"chronicles", "codex"}
    seen_stems = set()
    files = []

    for dirpath, _, filenames in os.walk(root_dir):
        rel_dir = os.path.relpath(dirpath, root_dir)
        if rel_dir == ".":
            continue

        source_type = rel_dir.split(os.sep)[0].lower()

        for fname in filenames:
            ext = os.path.splitext(fname)[1].lower()
            if ext not in SUPPORTED_EXTS:
                continue

            stem = os.path.splitext(fname)[0].lower()
            key = (source_type, stem)

            if ext == ".pdf" and source_type in DEDUPE_FOLDERS and key in seen_stems:
                continue

            full_path = os.path.join(dirpath, fname)
            files.append((full_path, source_type))
            seen_stems.add(key)

    return files

def run(input_dir, limit=None, dry_run=False):
    files = collect_files(input_dir)
    if limit:
        files = files[:limit]

    print(f"Found {len(files)} files to process.")

    all_documents = []
    parse_failures = []

    for path, source_type in files:
        filename = os.path.basename(path)
        try:
            docs = load_document(path, source_type)
        except Exception as e:
            parse_failures.append(f"{filename}: {type(e).__name__}: {e}")
            continue

        if not docs:
            parse_failures.append(f"{filename}: parsed successfully but produced no text (empty doc?)")
            continue

        all_documents.extend(docs)

    print(f"Loaded {len(all_documents)} document pieces from {len(files) - len(parse_failures)} files.")
    print(f"{len(parse_failures)} files failed to parse.")

    all_chunks = chunk_documents(all_documents)
    print(f"Produced {len(all_chunks)} chunks total.")

    write_limitations_log(parse_failures)

    if dry_run:
        print("Dry run — skipping embedding step.")
        return all_chunks

    if all_chunks:
        embed_and_store_chunks(all_chunks)

    return all_chunks


def write_limitations_log(parse_failures, path="docs/limitations.md"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"\n## Ingestion run — {datetime.now().isoformat(timespec='seconds')}\n\n")
        f.write(f"### Files that failed to parse ({len(parse_failures)})\n")
        if parse_failures:
            for line in parse_failures:
                f.write(f"- {line}\n")
        else:
            f.write("- None.\n")
    print(f"Limitations log updated: {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw", help="Root folder of raw documents")
    parser.add_argument("--limit", type=int, default=None, help="Only process the first N files (for testing)")
    parser.add_argument("--dry-run", action="store_true", help="Parse and chunk but skip embedding")
    args = parser.parse_args()

    run(args.input, limit=args.limit, dry_run=args.dry_run)