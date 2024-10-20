from src.config import Config as cg
from src.vector_store.databases.chroma_db import ChromaDB
from src.document_manager.manager import DocumentManager
from langchain_community.embeddings.ollama import OllamaEmbeddings

class VectorStore:
    """Vector store class to manage documents and their embeddings"""

    def __init__(self):
        self.document_manager = DocumentManager()
        self.database_manager = ChromaDB()

    def run(self):
        """Generates a vector database"""
        chunks = self.document_manager.process_document(cg.DOCUMENT_PATH.value)
        self.database_manager.build_database(chunks)
