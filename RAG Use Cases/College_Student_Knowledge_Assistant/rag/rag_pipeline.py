from retrieval.hybrid_search import hybrid_search

def generate_answer(query):

    docs = hybrid_search(query)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    answer = f"Answer based on retrieved documents:\n{context}"

    return answer, docs
