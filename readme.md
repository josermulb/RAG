# Basic local RAG

## Context

This is my implementation of a Retrieval Augmented Generation over a whole book.
The implementation currently supports Ollama as engine and runs local inference.
The vector database is built with chromadb.
My default prompts and questions are in spanish.

## Install:

This is developed with ```Python 3.12.4```

Create virtual environment
```
python -m venv env_RAG
```
Activate the environment
- In windows
```
.\env_RAG\Scripts\activate
```

Install requirements
```
pip install -r requirements.txt
```

## Configuration

All the required parameters are set in the ```src/config.py``` file.
- LLM_MODEL_ID : model identifier  (im using llama3.2)
- DOCUMENT_PATH: path to the document you want to add to the retrieval database
- VALID_DOCUMENT_TYPES: List of current valid document formats accepted (txt, pdf, docx)...
- RECURSIVE_SPLIT_PARAMETERS: parameters for splitting the documents into chunks
- CHROMA_DB_PATH : path where the chromadb database is saved
- AVAILABLE_EMBEDDINGS: List of available embeddings models
- EMBEDDINGS_PARAMETERS: Parameters for the embeddings generation model.
- LLM_INFERENCE_ENGINE: Engine used for the LLM infence (Currently ollama)
- TOP_K_RETRIEVAL: Number of chunks to retrieve.
- CHOSEN_TEMPLATE: Template chosen for the prompt
- INFERENCE_PARAMETERS: Parameters for the inference engine