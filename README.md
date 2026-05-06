# RAG-Based Customer Support Assistant (LangGraph + HITL)

## Project Overview
This project presents a Retrieval-Augmented Generation (RAG) based Customer Support Assistant that enables users to upload PDF documents dynamically and interact with them through context-aware queries.

Unlike traditional static systems, this solution processes user-provided documents in real time, retrieves relevant information, and generates accurate, grounded responses using a Large Language Model (LLM).

## Key Features

### Dynamic PDF Upload
- Supports real-time document uploads
- Eliminates dependency on preloaded datasets

### Context-Aware Retrieval
- Utilizes embeddings to identify relevant content
- Ensures responses are grounded in the uploaded documents

### Vector Storage with ChromaDB
- Efficient storage of embeddings
- Enables fast and scalable similarity search

### Session-Based Isolation
- Maintains separate contexts for each user session
- Prevents data leakage between different document uploads

### LangGraph Workflow
- Implements graph-based control flow for decision-making
- Supports intelligent routing: Answer, Clarify, Fallback, and Escalate

### Human-in-the-Loop (HITL)
- Handles ambiguous or complex queries
- Enables escalation to human intervention when necessary

### Streamlit Interface
- Provides a clean and interactive user interface
- Simplifies document upload and query interaction

## System Architecture

User → Upload PDF → Text Extraction → Chunking → Embeddings → ChromaDB → Retrieval → LLM → Response

## Tech Stack

- Python
- LangChain
- LangGraph
- ChromaDB
- Streamlit
- Hugging Face / Groq LLM
- PyPDF

## Installation and Usage

pip install -r requirements.txt  
streamlit run app/main.py

## Workflow

1. User uploads a PDF document
2. System extracts and processes the text
3. Text is divided into chunks for efficient handling
4. Embeddings are generated and stored in ChromaDB
5. User submits a query
6. Relevant document chunks are retrieved
7. LLM generates a context-aware response

## Example Queries

- What is the document about?
- Provide a summary of the document
- What are the key insights?

## Limitations

- Performance may vary depending on document size and complexity
- Requires proper embedding configuration for production-level deployment

## Future Enhancements

- Support for multi-document querying
- Integration of conversational memory
- Cloud-based deployment
- Enhanced user interface and experience

## Use Cases

- Customer Support Automation
- Document-Based Question Answering
- Knowledge Assistant Systems

## Conclusion

This project demonstrates the practical application of RAG architecture in building intelligent, context-aware assistants capable of handling real-world document-driven queries with efficiency and accuracy.
