from dataclasses import dataclass
from typing import List
import numpy as np
import ollama
from flask import Flask, render_template, request, jsonify
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@dataclass
class Document:
    id: str
    text: str
    source: str = ""

def load_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    chunks = [c.strip() for c in content.split("\n\n") if len(c.strip()) > 20]

    docs = []
    for i, chunk in enumerate(chunks):
        docs.append(Document(
            id=f"text_chunk_{i}",
            text=chunk,
            source=filepath   # ✅ automatically uses legal.txt
        ))
    return docs



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


def ask_ollama(model_name, query, context):
    prompt = f"""
You are a helpful assistant.

Use the provided context if it is relevant to the question.
If the context does not contain the answer, use your own knowledge to answer accurately.

Context:
{context}

Question: {query}

Answer:
"""

    response = ollama.generate(
        model=model_name,
        prompt=prompt,
        stream=False
    )

    return response["response"]


# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# Global variables for RAG
rag_system = None
model_name = "phi3"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/search', methods=['POST'])
def api_search():
    try:
        data = request.json
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({'error': 'Query cannot be empty'}), 400
        
        # Retrieve relevant documents
        results = rag_system.retrieve(query, top_k=3)
        
        if not results:
            return jsonify({
                'answer': 'No matching content found in the documents.',
                'sources': []
            })
        
        # Combine top chunks into context
        context = "\n\n".join([doc.text for doc, _ in results])
        
        # Get answer from Ollama
        final_answer = ask_ollama(model_name, query, context)
        
        # Prepare sources for response
        sources = [{'text': doc.text, 'score': score} for doc, score in results]
        
        return jsonify({
            'answer': final_answer,
            'sources': sources
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def main():
    global rag_system
    
    print("=== Loading RAG System ===")
    
    # Load documents
    docs = load_text_file("legal.txt")

    print(f"✅ Loaded {len(docs)} document chunks")
    
    # Initialize RAG
    rag_system = SimpleTfidfRAG(docs)
    print("✅ RAG system initialized")
    
    # Start Flask server
    print("\n🚀 Starting web server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    app.run(debug=False, host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()
