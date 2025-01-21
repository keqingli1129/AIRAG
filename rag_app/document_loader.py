"""
Handles loading web pages using LangChain's WebBaseLoader
"""

from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain_core.documents import Document
from typing import List

def load_webpage(url: str) -> List[Document]:
    """
    Loads a webpage and returns LangChain Document objects
    
    Args:
        url: The URL of the webpage to load
        
    Returns:
        List of Document objects containing the webpage content
    """
    # Create loader with BeautifulSoup config to parse main content
    loader = WebBaseLoader(
        web_paths=[url],
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("main-content", "article", "post-content", "content")
            )
        ),
        requests_kwargs={"headers": {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}}
    )
    
    # Load the documents
    documents = loader.load()
    
    # Print the contents
    for doc in documents:
        print("\n=== Document Content ===\n")
        print(doc.page_content)
        print("\n=====================\n")
        
    return documents
