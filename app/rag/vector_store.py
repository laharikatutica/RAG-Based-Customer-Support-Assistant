from langchain_community.vectorstores import Chroma
from config import CHROMA_DIR

def create_collection(chunks, embeddings, session_id):
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=session_id,
        persist_directory=CHROMA_DIR
    )

def load_collection(embeddings, session_id):
    return Chroma(
        collection_name=session_id,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR
    )