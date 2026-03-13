def format_citations(docs):

    citations = []

    for doc in docs:
        source = doc.metadata.get("source", "Unknown Source")
        citations.append(source)

    return citations
