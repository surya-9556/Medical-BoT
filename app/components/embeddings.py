from langchain_huggingface import HuggingFaceEmbeddings
from app.common import logger, custom_exception

logger = logger.get_logger(__name__)
c_exception = custom_exception.CustomException

def get_embedding_model():
    try:
        logger.info("Initializing the huggingface embedding model")
        model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        logger.info("Successfully loaded the model...")

        return model
    except Exception as e:
        error_message=c_exception("Error on loading the model", e)
        logger.error(f"Unable to load the embedding model {error_message}")
        return []