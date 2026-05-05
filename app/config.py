import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

CHUNK_SIZE = 700
CHUNK_OVERLAP = 100
TOP_K = 3
SIMILARITY_THRESHOLD = 0.3

MODEL_NAME = "llama3-8b-8192"

UPLOAD_DIR = "uploads"
CHROMA_DIR = "chroma_db"