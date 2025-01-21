"""
Main entry point for the RAG application.
Provides command line interface for loading web pages and asking questions.
"""

import argparse
import os
from dotenv import load_dotenv
from rag_app.document_loader import load_webpage
from rag_app.indexing import index_document
from rag_app.querying import query_document

def main():
    """
    Main function that:
    - Parses command line arguments
    - Handles the interaction loop
    - Coordinates loading, indexing and querying
    """
    # Load environment variables
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("Please set OPENAI_API_KEY in your .env file")
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Load a webpage and ask questions about its content"
    )
    parser.add_argument("url", help="URL of the webpage to load")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Load the webpage
    documents = load_webpage(args.url)

if __name__ == "__main__":
    main()
