from langchain_ollama import ChatOllama
from src.config import Config as cg

class Ollama:
    def __init__(self):
        self.model = ChatOllama(**cg.INFERENCE_PARAMETERS.value)
    
    def run_inference(self, prompt:str) -> str:
        return self.model.invoke(prompt)