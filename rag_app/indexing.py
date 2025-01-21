"""
Handles document splitting and vector store indexing
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import VectorStore
from langchain_core.documents import Document
from typing import List

def index_document(docs: List[Document]) -> VectorStore:
    """
    Splits documents and stores them in vector store
    """
    # TODO: Implement document indexing
