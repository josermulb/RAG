import os

from src.document_manager.loader import DocumentLoader
from src.document_manager.splitter import DocumentSplitter
from langchain_core.documents.base import Document
from src.config import Config as cg

class DocumentManager:

    def __init__(self):
        self.document_loader = DocumentLoader()
        self.document_splitter = DocumentSplitter()

    def process_document(self, document_path="", ) -> list[Document]:

        documents = self.document_loader.load_document(document_path)
        chunks = self.document_splitter.split_recursive(
            documents,
            cg.RECURSIVE_SPLIT_PARAMETERS.value)
        
        return chunks