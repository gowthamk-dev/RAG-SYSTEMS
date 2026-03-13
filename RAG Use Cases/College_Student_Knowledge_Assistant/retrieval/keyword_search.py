from rank_bm25 import BM25Okapi

def keyword_search(query, documents):

    tokenized_docs = [doc.page_content.split() for doc in documents]

    bm25 = BM25Okapi(tokenized_docs)

    scores = bm25.get_scores(query.split())

    return scores
