from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config import VECTOR_DB_PATH, EMBEDDING_MODEL

def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    # Note: In newer version of Chroma, persist is handled automatically or via client
    # db.persist() 

    print("Vector database created")
