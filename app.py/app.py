"""
SyllabusPilot — Streamlit Runner & Bridge
Embeds and serves the Google AI Studio React application inside Streamlit.
"""

import os
import streamlit as st
from dotenv import load_dotenv

# ── Load Environment Variables Safely ─────────────────────────────────────────
load_dotenv()
env_nested_path = os.path.join(os.path.dirname(__file__), "..", ".env", ".env")
if os.path.exists(env_nested_path):
    load_dotenv(dotenv_path=env_nested_path)

st.set_page_config(
    page_title="SyllabusPilot — AI University Study Planner",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Minimal Streamlit Header styling ──────────────────────────────────────────
st.markdown(
    """
    <style>
    #MainMenu, footer, header { visibility: hidden; }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
        width: 100% !important;
        height: 100vh !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Read static/index.html
index_file = os.path.join(os.path.dirname(__file__), "..", "static", "index.html")
if os.path.exists(index_file):
    with open(index_file, "r", encoding="utf-8") as f:
        html_code = f.read()
    st.components.v1.html(html_code, height=980, scrolling=True)
else:
    st.error("Static files not found at static/index.html")
