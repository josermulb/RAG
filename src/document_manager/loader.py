import os

from src.config import Config as cg
from langchain_core.documents.base import Document
from langchain_community.document_loaders import TextLoader



class DocumentLoader:
    def __init__(self) -> None:
        pass

    def load_txt(self, filepath: str) -> list[Document]:
        """
        Loads a txt and returns it as a langchain Document
        """
        loader = TextLoader(filepath, encoding='utf-8')
        document = loader.load()
        return document

    def evaluate_document_type(self, document_path:str) -> str:
        """
        Given a document path, extracts the document type and evaluates if it 
        is supported.
        """
        document_type = os.path.splitext(document_path)[-1]
        if document_type not in cg.VALID_DOCUMENT_TYPES.value:
            error_msg = f"""
            You provided an unsupported file type.
            Supported types are:
               {cg.VALID_DOCUMENT_TYPES.value}
            """
            raise ValueError(error_msg)
        return document_type
    
    def load_document(self, document_path:str) -> list[Document]:
        """
        Given a document path, loads a document as a langchain Document
        """
        if not document_path:
            raise ValueError("Please provide a document path.")
        else:
            document_type = self.evaluate_document_type(document_path)
            if document_type == ".txt":
                return self.load_txt(document_path)
            else:
                raise ValueError("No document loaded")