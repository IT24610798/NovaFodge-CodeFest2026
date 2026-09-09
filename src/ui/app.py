import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
from theme import inject_css, PRIMARY

# ---------- INTEGRATION POINT: Person 2's real search loop ----------
try:
    from src.search.agent_loop import run_agentic_search
    BACKEND_READY = True
    BACKEND_ERROR = None
except Exception as e:

    BACKEND_READY = False
    BACKEND_ERROR = str(e)

    def run_agentic_search(*args, **kwargs):
        raise RuntimeError(f"Backend not available: {BACKEND_ERROR}")

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="Ashen Era Archive Assistant",
    page_icon="📜",
    layout="wide",
)
inject_css()

if not BACKEND_READY:
    st.warning(
        "⚠️ Heads up: the search backend didn't load correctly, so answers "
        "won't work until this is fixed.\n\n"
        f"Technical detail: `{BACKEND_ERROR}`\n\n"
        "Common fixes: check the OpenRouter API key is set, or that "
        "ChromaDB/the sample data has been built."
    )

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown(f"<h2 style='color:{PRIMARY};'>📜 Ashen Era Archive</h2>", unsafe_allow_html=True)
    st.caption("Agentic search assistant · Sub-track 1C")
    st.divider()
    show_reasoning = st.toggle("Show search steps", value=True,
                                help="Show the assistant's search/reflect/search process")
    max_iterations = st.slider("Max search iterations", min_value=1, max_value=5, value=3,
                                help="How many search->reflect rounds the agent can use")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.divider()

    # ---- Example questions (edit these to match your actual corpus!) ----
    st.caption("Try asking:")
    EXAMPLE_QUESTIONS = [
        "Who is Ashvael and what happened to the Cindered Accord?",
        "What caused the War of Broken Sigils?",
        "Describe the political structure after the Ashen Era began.",
    ]
    for eq in EXAMPLE_QUESTIONS:
        if st.button(eq, use_container_width=True, key=f"example_{eq}"):
            st.session_state.pending_question = eq

    st.divider()
    st.caption("Team: [Your Team Name]")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


def chunk_source_label(chunk: dict) -> str:
    """
    Chunks from HybridSearcher may label their origin document differently
    depending on how Person 1 built the ingestion pipeline. Try common
    field names in order, and fall back to the chunk id if none match.
    """
    for key in ("source", "document", "doc_name", "filename", "title"):
        if chunk.get(key):
            return str(chunk[key])
    return f"chunk {chunk.get('id', '?')}"


def render_steps(search_history: list, is_sufficient: bool, container=None):
    """Render the query history as a reasoning trail."""
    target = container if container is not None else st
    with target.expander("🔍 How I searched for this", expanded=False):
        for i, query in enumerate(search_history, start=1):
            st.markdown(
                f"""<div class="search-step done">
                <div class="step-label">Search {i}</div>
                Query: "{query}"
                </div>""",
                unsafe_allow_html=True,
            )
        status = "Enough information was found." if is_sufficient else \
                 "Reached max iterations before being fully confident."
        st.caption(status)


# ---------- RENDER PAST MESSAGES ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant" and msg.get("search_history") and show_reasoning:
            render_steps(msg["search_history"], msg.get("is_sufficient", True))
        st.markdown(msg["content"])
        if msg.get("sources"):
            chips = "".join(f'<span class="source-chip">📄 {s}</span>' for s in msg["sources"])
            st.markdown(chips, unsafe_allow_html=True)

def ask(question: str):
    """Runs one question through the real backend and stores the result."""
    with st.chat_message("assistant"):
        with st.spinner("🔍 Digging through the archive... (search → reflect → search)"):
            try:
                result_state = run_agentic_search(question, max_iterations=max_iterations)
                error = None
            except Exception as e:
                result_state = None
                error = str(e)

        if error:
            st.error(
                "😕 The search hit a snag and couldn't finish.\n\n"
                "This usually means the free LLM API is temporarily rate-limited, "
                "or slow to respond. Try again in a few seconds using the button below."
            )
            if st.button("🔁 Try again", key=f"retry_{len(st.session_state.messages)}"):
                st.session_state.pending_question = question
                st.rerun()
            with st.expander("Technical details"):
                st.code(error)
        else:
            if show_reasoning:
                render_steps(result_state.search_history, result_state.is_sufficient)

            st.markdown(result_state.final_answer)

            sources = [chunk_source_label(c) for c in result_state.retrieved_chunks]
            sources = list(dict.fromkeys(sources)) 
            if sources:
                chips = "".join(f'<span class="source-chip">📄 {s}</span>' for s in sources)
                st.markdown(chips, unsafe_allow_html=True)

            st.session_state.messages.append({
                "role": "assistant",
                "content": result_state.final_answer,
                "search_history": result_state.search_history,
                "is_sufficient": result_state.is_sufficient,
                "sources": sources,
                "question": question, 
            })


# ---------- CHAT INPUT ----------
typed_question = st.chat_input(
    "Ask a question about the Ashen Era Archive..." if BACKEND_READY else "Backend not connected - see warning above",
    disabled=not BACKEND_READY,
)

question = typed_question or st.session_state.pending_question
st.session_state.pending_question = None  

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    ask(question)


if st.session_state.messages and st.session_state.messages[-1]["role"] == "assistant":
    last = st.session_state.messages[-1]
    if last.get("question") and st.button("🔁 Regenerate this answer"):
        st.session_state.messages.pop()  
        with st.chat_message("user"):
            st.markdown(last["question"])
        ask(last["question"])