from langchain_core.documents.base import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentSplitter:

    def __init__(self) -> None:
        pass

    def split_recursive(self, documents: list[Document], split_params: dict) -> list[Document]:
        """
        Splits langchain documents into chunks.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            **split_params
        )
        return text_splitter.split_documents(documents)