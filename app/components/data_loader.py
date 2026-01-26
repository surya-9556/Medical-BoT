import os
from app.components.pdf_loader import load_pdf_files, create_text_chunks
from app.components.vector_store import save_vector_store
from app.config.config import DB_FAISS_PATH
from app.common import logger, custom_exception

logger = logger.get_logger(__name__)
c_exception = custom_exception.CustomException

def process_and_store_doc():
    try:
        logger.info("Creating the vectorstore...")

        docs = load_pdf_files()
        text_chunks = create_text_chunks(docs)
        save_store = save_vector_store(text_chunks)

        logger.info("Vector store created successfully...")

        return save_store

    except Exception as e:
        error_message = c_exception('Failed to save/create the vectorstore',e)
        logger.error(str(error_message))
        return []
    
if __name__ == "__main__":
    process_and_store_doc()