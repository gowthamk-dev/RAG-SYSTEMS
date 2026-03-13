from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import VECTOR_DB_PATH, EMBEDDING_MODEL, TOP_K_RESULTS

def semantic_search(query):

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    db = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    results = db.similarity_search(query, k=TOP_K_RESULTS)

    return results
