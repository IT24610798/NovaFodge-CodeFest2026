from src.search.LLM_client import call_llm


def reflect(question: str, retrieved_chunks: list) -> dict:
    # build a readable summary of what we've found so far
    context_text = "\n\n".join(
        f"[{c['id']}] {c['text']}" for c in retrieved_chunks
    )

    prompt = f"""You are helping answer a question using retrieved document chunks.

QUESTION: {question}

RETRIEVED CHUNKS:
{context_text}

Decide if the chunks above contain ENOUGH information to fully and confidently answer the question.

Respond in EXACTLY this format, nothing else:
SUFFICIENT: yes or no
NEW_QUERY: (only if SUFFICIENT is no) a better, more specific search query to try next
"""

    response = call_llm(prompt)
    return parse_reflection(response)


def parse_reflection(response: str) -> dict:
    is_sufficient = "SUFFICIENT: yes" in response.lower().replace(" ", "").replace(":", ": ") or "sufficient: yes" in response.lower()
    
    # simpler, more reliable check:
    is_sufficient = "yes" in response.lower().split("sufficient:")[1].split("\n")[0] if "sufficient:" in response.lower() else False

    new_query = None
    if "new_query:" in response.lower():
        new_query = response.lower().split("new_query:")[1].strip().split("\n")[0]

    return {
        "is_sufficient": is_sufficient,
        "new_query": new_query,
        "raw_response": response,
    }


if __name__ == "__main__":
    from src.search.hybrid_search import HybridSearcher

    searcher = HybridSearcher()
    question = "Who is Ashvael?"
    results = searcher.search(question, top_k=3)

    decision = reflect(question, results)
    print("Is sufficient:", decision["is_sufficient"])
    print("New query:", decision["new_query"])
    print("\n--- Raw AI response ---")
    print(decision["raw_response"])