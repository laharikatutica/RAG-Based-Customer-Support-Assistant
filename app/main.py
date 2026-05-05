import streamlit as st

st.set_page_config(page_title="RAG App")

st.title("RAG Customer Support Assistant")

# Try loading UI safely
try:
    from ui.streamlit_app import run_app
    run_app()
except Exception as e:
    st.error(f"Error loading app: {e}")