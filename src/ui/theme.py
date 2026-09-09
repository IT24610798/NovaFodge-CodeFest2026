PRIMARY = "#7C3AED"   
PRIMARY_LIGHT = "#A78BFA"  
BACKGROUND = "#0F0F14"     
SURFACE = "#1A1A24"        
SURFACE_LIGHT = "#25252F"  
TEXT = "#F2F2F5"
TEXT_MUTED = "#9999A5"     
SUCCESS = "#22C55E"        
WARNING = "#F59E0B"        
BORDER = "#2E2E3A"        



def inject_css():
    """Call this once at the top of app.py to apply the theme everywhere."""
    import streamlit as st

    st.markdown(
        f"""
        <style>
        /* Overall app background */
        .stApp {{
            background-color: {BACKGROUND};
        }}

        /* Chat message bubbles */
        [data-testid="stChatMessage"] {{
            background-color: {SURFACE};
            border: 1px solid {BORDER};
            border-radius: 12px;
            padding: 4px 8px;
        }}

        /* Reasoning / search-step card */
        .search-step {{
            background-color: {SURFACE};
            border-left: 3px solid {PRIMARY};
            border-radius: 8px;
            padding: 10px 14px;
            margin-bottom: 8px;
            color: {TEXT};
        }}
        .search-step.done {{
            border-left-color: {SUCCESS};
        }}
        .search-step.active {{
            border-left-color: {WARNING};
        }}
        .search-step .step-label {{
            color: {TEXT_MUTED};
            font-size: 0.8em;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        /* Source citation chip */
        .source-chip {{
            display: inline-block;
            background-color: {SURFACE_LIGHT};
            color: {PRIMARY_LIGHT};
            border: 1px solid {BORDER};
            border-radius: 999px;
            padding: 2px 10px;
            margin: 2px 4px 2px 0;
            font-size: 0.8em;
        }}

        /* Buttons */
        .stButton > button {{
            background-color: {PRIMARY};
            color: white;
            border-radius: 8px;
            border: none;
        }}
        .stButton > button:hover {{
            background-color: {PRIMARY_LIGHT};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )