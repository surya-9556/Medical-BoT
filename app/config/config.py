import os

HF_TOKEN = os.environ.get('HF_TOKEN')
GROQ_API_KEY = os.environ.get("GROQ_API")

HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
DB_FAISS_PATH="Vectorstore/df_faiss"
DATA_PATH="data/"
CHUNK_SIZE=1000
CHUNK_OVERLAP=200