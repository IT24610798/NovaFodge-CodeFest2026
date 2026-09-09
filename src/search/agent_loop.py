from src.search.state import SearchState
from src.search.hybrid_search import HybridSearcher
from src.search.reflect import reflect
from src.search.LLM_client import call_llm


def run_agentic_search(question: str, max_iterations: int = 3) -> SearchState:
    state = SearchState(question, max_iterations=max_iterations)
    searcher = HybridSearcher()

    while state.has_iterations_left() and not state.is_sufficient:
        # 1. SEARCH using the current query (starts as the original question)
        results = searcher.search(state.current_query, top_k=5)
        state.add_chunks(results)
        state.record_search(state.current_query)

        # 2. REFLECT - do we have enough to answer?
        decision = reflect(state.original_question, state.retrieved_chunks)
        state.is_sufficient = decision["is_sufficient"]

        # 3. If not enough, and we have iterations left, try a better query
        if not state.is_sufficient and decision["new_query"] and state.has_iterations_left():
            state.current_query = decision["new_query"]

    # 4. ANSWER - generate the final answer using everything we found
    state.final_answer = generate_final_answer(state)
    return state


def generate_final_answer(state: SearchState) -> str:
    context_text = "\n\n".join(
        f"[{c['id']}] {c['text']}" for c in state.retrieved_chunks
    )

    prompt = f"""Answer the question using ONLY the information in the context below.
If the context doesn't fully answer it, say what is known and note what's missing.

QUESTION: {state.original_question}

CONTEXT:
{context_text}

ANSWER:"""

    return call_llm(prompt)


if __name__ == "__main__":
    question = "Who is Ashvael and what happened to the Cindered Accord?"
    result_state = run_agentic_search(question)

    print("=== SEARCH HISTORY ===")
    print(result_state.search_history)
    print("\n=== ITERATIONS USED ===")
    print(result_state.iteration)
    print("\n=== FINAL ANSWER ===")
    print(result_state.final_answer)