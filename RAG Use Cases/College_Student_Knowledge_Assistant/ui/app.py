import streamlit as st
import os
import sys

# Add root directory to path so imports work correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rag.rag_pipeline import generate_answer
from utils.citation_formatter import format_citations

st.set_page_config(page_title="College Student Knowledge Assistant", layout="wide")

st.title("🎓 College Student Knowledge Assistant")
st.markdown("### Ask any question about college policies, syllabus, or administrative tasks.")

query = st.text_input("Ask your question here:", placeholder="e.g., What is the minimum attendance requirement?")

if query:
    with st.spinner("Searching official documents..."):
        try:
            answer, docs = generate_answer(query)
            
            st.markdown("---")
            st.markdown("#### Research-Based Answer")
            st.write(answer)

            st.markdown("---")
            st.markdown("#### Document Citations")
            citations = format_citations(docs)
            
            for i, c in enumerate(citations):
                st.info(f"Source {i+1}: {os.path.basename(c)}")
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Make sure you have ingested documents into the vector store first.")

st.sidebar.title("System Info")
st.sidebar.info("This RAG system retrieves information from official college documents to provide accurate answers.")
