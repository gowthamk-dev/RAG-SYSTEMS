from ingestion.load_documents import load_documents
from ingestion.chunk_documents import split_documents
from ingestion.create_embeddings import create_vector_store
import os

def main():
    print("🚀 Starting Document Ingestion Pipeline...")
    
    # 1. Load Documents
    print("📂 Loading documents from data/ directory...")
    documents = load_documents()
    
    if not documents:
        print("❌ No documents found. Please add PDF or TXT files to the data/ directories.")
        return

    print(f"✅ Loaded {len(documents)} document pages.")

    # 2. Chunk Documents
    print("✂️ Splitting documents into chunks...")
    chunks = split_documents(documents)
    print(f"✅ Created {len(chunks)} chunks.")

    # 3. Create Vector Store
    print("🧠 Creating vector embeddings and storing in ChromaDB...")
    create_vector_store(chunks)
    print("✨ Ingestion complete! You can now run the UI.")

if __name__ == "__main__":
    main()
