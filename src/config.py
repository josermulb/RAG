import os
from dotenv import load_dotenv
from enum import Enum
load_dotenv()

class Config(Enum):
    # LLM model ID
    LLM_MODEL_ID = 'llama3.2'

    # Documents load parameters
    DOCUMENT_PATH = os.getenv('DOCUMENT_PATH')
    VALID_DOCUMENT_TYPES = [".txt"]
    RECURSIVE_SPLIT_PARAMETERS = {
        'chunk_size':800,
        'chunk_overlap':80,
        'length_function':len,
        'is_separator_regex':False,
    }

    # Retrieval DB database
    CHROMA_PATH = os.path.join('data','chroma')
    AVAILABLE_EMBEDDINGS = ["llama3.2"]
    EMBEDDINGS_PARAMETERS = {'model':LLM_MODEL_ID}

    # Inference parameters
    LLM_INFERENCE_ENGINE = 'ollama'

    # Retrieval
    TOP_K_RETRIEVAL = 5

    # Inference parameters
    CHOSEN_TEMPLATE = 'BASE_TEMPLATE'
    INFERENCE_PARAMETERS = {
        'model': LLM_MODEL_ID,
        'temperature': 0.3,
    }

    

class TemplatesStrings(Enum):
    BASE_TEMPLATE = """
    Te voy a pasar el siguiente contexto que corresponde a fragmentos de un libro:
    {context}
    
    ---

    Responde a la pregunta siguiente basándote en el contexto proporcionado: {question}
    """