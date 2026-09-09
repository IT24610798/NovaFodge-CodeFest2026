"""
chunker.py — splits document text into smaller overlapping chunks
("index cards" in the analogy).

Takes the output of loaders.load_document() directly — each item already
has text, filename, source_type, reliability_tier, and page_number attached.
"""

import uuid


def chunk_text(text, chunk_size=800, overlap=100):
    """Split a block of text into overlapping chunks."""
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def chunk_documents(documents, chunk_size=800, overlap=100):
    """
    documents: list of dicts as produced by loaders.load_document()
    Returns final chunk objects ready for embed_and_store.py
    """
    final_chunks = []
    for doc in documents:
        pieces = chunk_text(doc["text"], chunk_size=chunk_size, overlap=overlap)
        for i, piece in enumerate(pieces):
            chunk = {
                "id": str(uuid.uuid4()),
                "text": piece,
                "metadata": {
                    "source": doc["filename"],
                    "page": doc["page_number"] if doc["page_number"] is not None else 1,
                    "chunk_index": i,
                    "doc_type": doc["source_type"],
                    "reliability_tier": doc["reliability_tier"],
                },
            }
            final_chunks.append(chunk)
    return final_chunks