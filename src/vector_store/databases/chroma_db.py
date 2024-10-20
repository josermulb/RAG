from src.config import Config as cg
from src.vector_store.embedding_manager import EmbeddingManager

from llama_index.core import Document
from langchain_community.vectorstores.chroma import Chroma

class ChromaDB:
    def __init__(self):
        self.embedding_manager = EmbeddingManager()

    def calculate_chunk_ids(self, chunks: list[Document]) -> list[Document]:
        """
        Assigns an ID to each chunk.
        Function from 'https://github.com/pixegami/rag-tutorial-v2'
        """
        last_page_id = None
        current_chunk_index = 0
        for chunk in chunks:
            source = chunk.metadata.get("source")
            page = chunk.metadata.get("page")
            current_page_id = f"{source}:{page}"
            if current_page_id == last_page_id:
                current_chunk_index += 1
            else:
                current_chunk_index = 0
            chunk_id = f"{current_page_id}:{current_chunk_index}"
            last_page_id = current_page_id
            chunk.metadata["id"] = chunk_id
        return chunks
    
    def build_database(self, chunks: list[Document]):
        """
        Generates a chroma db and add each chunk if it does not already exists.
        Function named 'add_to_chroma' from 'https://github.com/pixegami/rag-tutorial-v2'
        """
        db = Chroma(
            persist_directory=cg.CHROMA_PATH.value,
            embedding_function=self.embedding_manager.get_embedding_function()
        )
        chunks_with_ids = self.calculate_chunk_ids(chunks)
        existing_items = db.get(include=[]) 
        existing_ids = set(existing_items["ids"])
        print(f"Number of existing documents in DB: {len(existing_ids)}")

        new_chunks = []
        for chunk in chunks_with_ids:
            if chunk.metadata["id"] not in existing_ids:
                new_chunks.append(chunk)

        if len(new_chunks):
            print(f"👉 Adding new documents: {len(new_chunks)}")
            new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
            db.add_documents(new_chunks, ids=new_chunk_ids)
            db.persist()
        else:
            print("✅ No new documents to add")