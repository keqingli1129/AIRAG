"""
Handles loading web pages using LangChain's WebBaseLoader
"""

from langchain_community.document_loaders import WebBaseLoader
import bs4

def load_webpage(url: str):
    """
    Loads a webpage and returns LangChain Document objects
    """
    # TODO: Implement webpage loading
