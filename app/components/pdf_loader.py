import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from app.common import logger, custom_exception
from app.config.config import DATA_PATH,CHUNK_SIZE,CHUNK_OVERLAP

logger = logger.get_logger(__name__)
c_exception = custom_exception.CustomException

def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise c_exception("Data path Not Exists")
        
        logger.info(f"Loading file from {DATA_PATH}")

        loader = DirectoryLoader(DATA_PATH,glob="*.pdf",loader_cls=PyPDFLoader)

        documents=loader.load()

        if not documents:
            logger.warning(f"No PDF's found in the diectory {DATA_PATH}")
        else:
            logger.info(f"Successfully found the document")

        return documents

    except Exception as e:
        error_message = c_exception("failed to load docs", e)
        logger.error(str(error_message))
        return []
    

def create_text_chunks(documents):
    try:
        if not documents:
            raise c_exception(f'documenet are not found')
        
        logger.info(f'Splitting {len(documents)} documents into chunks')

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)

        text_chunks = text_splitter.split_documents(documents)

        logger.info(f"Successfully generated the chunks of size {len(text_chunks)}")
        return text_chunks

    except Exception as e:
        error_message = c_exception("Failed to generate chunks", e)
        logger.error(str(error_message))
        return []