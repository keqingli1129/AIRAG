"""
Handles RAG query processing and answer generation
"""

from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_core.vectorstores import VectorStore

def query_document(question: str, vector_store: VectorStore) -> str:
    """
    Processes a question using RAG and returns an answer
    """
    # TODO: Implement RAG querying
