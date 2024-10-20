from src.config import Config as cg
from langchain_community.embeddings.ollama import OllamaEmbeddings

class EmbeddingManager:

    def __init__(self):
        self.embedding_processor = self.get_embedding_function()

    def get_embedding_function(self):
        """
        Returns the embedding processor based on the configuration settings.
        """
        # TODO: Add support for other embedding models
        return OllamaEmbeddings(**cg.EMBEDDINGS_PARAMETERS.value)