# College Student Knowledge Assistant (RAG)

This project implements a Retrieval-Augmented Generation (RAG) system for answering student queries using official college documents.

## Project Structure
- `data/`: Document corpus (PDFs)
- `ingestion/`: Scripts for loading, chunking, and indexing documents
- `retrieval/`: Search logic (Semantic, Keyword, Hybrid)
- `rag/`: RAG pipeline for answer generation
- `ui/`: Streamlit web interface
- `vector_store/`: ChromaDB persistent storage

## Setup Instructions

1.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Add Documents**:
    Place your college PDF documents in the `data/` subfolders (e.g., `data/handbook/`, `data/syllabus/`).

3.  **Ingest Documents**:
    You need a script to run the ingestion pipeline. (See `run_ingestion.py`)

4.  **Run the UI**:
    ```bash
    streamlit run ui/app.py
    ```

## Features
- **Document Ingestion**: Automatically loads and chunks PDFs.
- **Vector Embeddings**: Uses high-quality embeddings from Sentence-Transformers.
- **Semantic Search**: Understands the meaning of queries, not just keywords.
- **Citations**: Every answer includes the source document reference.
- **Modern UI**: Clean and responsive Streamlit interface.
