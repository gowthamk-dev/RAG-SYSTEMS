import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from config import DATA_PATH

def load_documents():
    documents = []

    for root, dirs, files in os.walk(DATA_PATH):
        for file in files:
            path = os.path.join(root, file)
            try:
                if file.endswith(".pdf"):
                    loader = PyPDFLoader(path)
                    docs = loader.load()
                    documents.extend(docs)
                elif file.endswith(".txt"):
                    loader = TextLoader(path)
                    docs = loader.load()
                    documents.extend(docs)
            except Exception as e:
                print(f"Error loading {file}: {e}")

    return documents
