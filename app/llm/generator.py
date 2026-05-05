from langchain_groq import ChatGroq
from config import MODEL_NAME

def get_llm():
    return ChatGroq(model_name=MODEL_NAME)


def generate_answer(llm, query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a customer support assistant.

Answer ONLY from the given context.
If answer is not present, say "Information not found in documents".

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)
    return response.content