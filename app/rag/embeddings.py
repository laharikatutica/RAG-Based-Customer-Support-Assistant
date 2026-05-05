from langchain_community.embeddings import FakeEmbeddings

def get_embeddings():
    return FakeEmbeddings(size=1536)