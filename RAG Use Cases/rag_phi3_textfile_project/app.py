from dataclasses import dataclass
from typing import List
import numpy as np
import ollama

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Document Structure
# -----------------------------
@dataclass
class Document:
    id: str
    text: str
    source: str = ""


# -----------------------------
# Load and Chunk Text File
# -----------------------------
def load_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    chunks = [c.strip() for c in content.split("\n\n") if len(c.strip()) > 20]

    docs = []
    for i, chunk in enumerate(chunks):
        docs.append(Document(
            id=f"text_chunk_{i}",
            text=chunk,
            source="CIT.txt"
        ))
    return docs


# -----------------------------
# TF-IDF RAG System
# -----------------------------
class SimpleTfidfRAG:
    def __init__(self, docs: List[Document]):
        self.docs = docs
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
        self.doc_matrix = self.vectorizer.fit_transform([d.text for d in docs])

    def retrieve(self, query, top_k=3):
        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.doc_matrix).flatten()
        idx = np.argsort(sims)[::-1][:top_k]
        return [(self.docs[i], float(sims[i])) for i in idx if sims[i] > 0]


# -----------------------------
# Ollama Query Function
# -----------------------------
def ask_ollama(model_name, query, context):
    prompt = f"""
You are a helpful assistant. Use ONLY the following context to answer.
If the information is not available, say:
'I could not find this in the provided document'.

Context:
{context}

Question: {query}

Answer:
"""

    response = ollama.generate(
        model=model_name,
        prompt=prompt
    )

    return response["response"]


# -----------------------------
# Main Program
# -----------------------------
def main():
    print("=== TF-IDF RAG + Ollama (Phi3 Ready) ===")

    docs = load_text_file("CIT.txt")
    rag = SimpleTfidfRAG(docs)

    model_name = "phi3"   # change if needed

    while True:
        query = input("\nHola ! Marhabaa , Search for CIT : ")

        if query.lower() == "exit":
            break

        # 🔥 Handle Counting Questions (Direct Python Logic)

        full_text = " ".join([doc.text for doc in docs])

        if "how many words" in query.lower():
            word_count = len(full_text.split())
            print("\n=== Final Answer ===")
            print(word_count)
            print("-----------------------------")
            continue

        if "how many dots" in query.lower():
            dot_count = full_text.count(".")
            print("\n=== Final Answer ===")
            print(dot_count)
            print("-----------------------------")
            continue

        # 🔎 Normal RAG Retrieval
        results = rag.retrieve(query)

        if not results:
            print("No matching content found")
            continue

        context = "\n\n".join([doc.text for doc, _ in results])

        print("\n🧠 Asking Ollama...")
        final_answer = ask_ollama(model_name, query, context)

        print("\n=== Final Answer ===")
        print(final_answer)
        print("-----------------------------")


# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    main()