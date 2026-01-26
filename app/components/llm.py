# from langchain_huggingface import HuggingFaceEndpoint
from langchain_groq import ChatGroq
from app.config.config import HF_TOKEN, HUGGINGFACE_REPO_ID, GROQ_API_KEY
from app.common import logger, custom_exception

logger = logger.get_logger(__name__)
c_exception = custom_exception.CustomException

print(GROQ_API_KEY)
def load_llm(model_name: str = "llama-3.1-8b-instant", groq_api_key: str = None):
    try:
        logger.info("Loading LLM from huggingface")

        # llm = ChatGroq(
        #     repo_id = hugging_face_repo,
        #     huggingfacehub_api_token = hf_token,
        #     task='conversational',
        #     temperature=0.2,
        #     max_new_tokens=256,
        #     return_full_text=False
        # )

        if groq_api_key is None:
            import os
            groq_api_key = os.getenv("GROQ_API")

        if not groq_api_key:
            raise c_exception("GROQ API key is missing. Set it in config or environment variable.")

        llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name=model_name,
            temperature=0.3,
            max_tokens=256,
        )

        logger.info("llm loaded successfully....")
        return llm
    except Exception as e:
        error_message = c_exception("Failed to load the llm",e)
        logger.error(str(error_message))
        return []
    