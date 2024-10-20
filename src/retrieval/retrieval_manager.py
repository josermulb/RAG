from src.vector_store.embedding_manager import EmbeddingManager
from langchain_core.documents.base import Document
from langchain_community.vectorstores.chroma import Chroma
from src.config import Config as cg

class RetrievalManager:

    def __init__(self, retrieval_engine:str):
        self.embedding_manager = EmbeddingManager()
        self.vector_db = self.get_retrieval_engine(retrieval_engine)

    def get_retrieval_engine(self, retrieval_engine):
        """
        Instanciates the desired retrieval engine.
        """
        if retrieval_engine =='chroma':
            return Chroma(
                persist_directory=cg.CHROMA_PATH.value,
                embedding_function=self.embedding_manager.get_embedding_function()
                )
        else:
            raise ValueError("Invalid retrieval engine selected")

    def retrieve_chunks(self, query:str, top_k:int)-> list[tuple[Document]]:
        """
        Retrieves top k chunks
        """
        return self.vector_db.similarity_search_with_score(query, k=top_k)
