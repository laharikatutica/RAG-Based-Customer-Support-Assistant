import streamlit as st
import os

from rag.pdf_ingestor import load_pdf
from rag.chunker import chunk_docs
from rag.embeddings import get_embeddings
from rag.vector_store import create_collection

def run_app():
    st.subheader("Upload PDF and Ask Questions")

    uploaded_file = st.file_uploader("Upload your PDF")

    if uploaded_file is not None:
        st.write("Processing PDF...")

        try:
            # Save file
            os.makedirs("uploads", exist_ok=True)
            file_path = os.path.join("uploads", uploaded_file.name)

            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            st.write("File saved")

            # Load PDF
            docs = load_pdf(file_path)
            st.write(f"Pages loaded: {len(docs)}")

            # Chunking
            chunks = chunk_docs(docs)
            st.write(f"Chunks created: {len(chunks)}")

            # Embeddings
            embeddings = get_embeddings()

            # Store
            vectorstore = create_collection(chunks, embeddings, "demo")

            # Save retriever
            st.session_state.retriever = vectorstore.as_retriever()

            st.success("PDF processed successfully!")

        except Exception as e:
            st.error(f"Error: {e}")

  
    # Question Section
    if "retriever" in st.session_state:
        query = st.text_input("Ask a question")

        if query:
            try:
                docs = st.session_state.retriever.invoke(query)

                if docs:
                    st.write("### Answer:")

                    # Combine top 3 chunks
                    combined = " ".join([doc.page_content for doc in docs[:3]])

                    # Clean formatting
                    combined = combined.replace("\n", " ")

                    # Make it readable (limit sentences)
                    sentences = combined.split(". ")
                    clean_answer = ""

                    for s in sentences[:5]:
                        clean_answer += s.strip() + ". "

                    st.write(clean_answer)

                else:
                    st.write("No relevant answer found")

            except Exception as e:
                st.error(f"Error during retrieval: {e}")