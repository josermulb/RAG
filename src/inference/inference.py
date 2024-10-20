from src.config import Config as cg
from src.inference.engines.ollama import Ollama

class InferenceManager:

    def __init__(self):
        self.inference_engine = self.get_inference_engine(
            cg.LLM_INFERENCE_ENGINE.value
            )

    def get_inference_engine(
            self, inference_engine:str
            ) -> object:
        """
        Instanciates the desired inference engine.
        """
        if inference_engine == "ollama":
            return Ollama()
        else:
            raise ValueError(
                "Invalid inference engine specified in the configuration file."
                )
    
    def run_inference(self, prompt: str) -> str:
        return self.inference_engine.run_inference(prompt)