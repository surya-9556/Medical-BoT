from langchain_community.vectorstores import FAISS
from app.components.embeddings import get_embedding_model
from app.common import logger, custom_exception
from app.config.config import DB_FAISS_PATH
import os

logger = logger.get_logger(__name__)
c_exception = custom_exception.CustomException

def load_vector_store():
    try:
        embedding_model = get_embedding_model()
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Loading exising vectorstore....")
            return FAISS.load_local(
                DB_FAISS_PATH,
                embedding_model,
                allow_dangerous_deserialization=True
            )
        
        else:
            logger.warning("No Vector Store Found.....")

    except Exception as e:
        error_message = c_exception("Failed to load vectorstore", e)
        logger.error(str(error_message))
        return []

def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise c_exception("No chunks were found....")
        
        logger.info("Creating a new vector store...")

        embedd_model = get_embedding_model()
        db = FAISS.from_documents(text_chunks,embedd_model)
        logger.info("Saving vectorstore...")
        db.save_local(DB_FAISS_PATH)
        logger.info("Successfully saved the embedded vector database set...")

    except Exception as e:
        error_message = c_exception("Failed to create a vectorstore...", e)
        logger.error(str(error_message))
        return []