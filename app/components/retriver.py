from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from app.components.llm import load_llm
from app.components.vector_store import load_vector_store
from app.common import logger, custom_exception

import os

logger = logger.get_logger(__name__)
c_exception = custom_exception.CustomException

CUSTOM_PROMPT_TEMPLATE = """
Answer the following medical question in 2-3 lines maximum using only the information provided from the following context.

Context: {context}

Question: {question}

Answer:
"""

def custom_prompt_temp():
    return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE,input_variables=["context","question"])

def create_retrival_chain():
    try:
        logger.info("Loading vector store for context...")
        db = load_vector_store()

        if db is None:
            raise c_exception("Vector store was not loaded successfully....")
        llm = load_llm()

        if llm is None:
            raise c_exception("LLM was not loaded successfully....")
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever = db.as_retriever(search_kwargs={'k':1}),
            return_source_documents=False,
            chain_type_kwargs={'prompt':custom_prompt_temp()}
        )

        logger.info("Successfully created the QA chain")
        return qa_chain

    except Exception as e:
        error_message = c_exception("Failed to create qa chain", e)
        logger.error(str(error_message))
        return None