from rag.rag_pipeline import generate_answer
import os
import sys

# Add root directory to path
sys.path.append(os.path.dirname(__file__))

def main():
    query = "What is the minimum attendance required?"
    print(f"❓ Query: {query}")
    
    answer, docs = generate_answer(query)
    print("\n💡 Answer:")
    print(answer)
    
    print("\n📚 Sources:")
    for doc in docs:
        print(f"- {os.path.basename(doc.metadata.get('source', 'Unknown'))}")

if __name__ == "__main__":
    main()
