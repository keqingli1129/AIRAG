"""
Main entry point for the RAG application.
Provides command line interface for loading web pages and asking questions.
"""

import argparse
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
    # TODO: Implement main function

if __name__ == "__main__":
    main()
