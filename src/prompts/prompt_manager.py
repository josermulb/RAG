from langchain.prompts import ChatPromptTemplate
from src.config import Config as cg
from src.config import TemplatesStrings as ts

class PromptManager:

    def __init__(self):
        self.templates_map = {
            f"{prompt.name}": prompt.value
            for prompt in ts
        }

    def get_template(self, template:str)-> ChatPromptTemplate:
        """
        Loads the desired template.
        """
        if template not in self.templates_map:
            error_msg = f"""
            Unsupported prompt template.
            Supported templates are:
                {[self.templates_map.keys()]}
            """
            raise ValueError(error_msg)
        else:
            return ChatPromptTemplate.from_template(
                self.templates_map[template]
                )

    def build_prompt(self, context_text: str, question_text: str) -> str:
        """
        Given the parameters builds the required prompt.
        """
        prompt_template = self.get_template(cg.CHOSEN_TEMPLATE.value)
        prompt = prompt_template.format(
            context=context_text, question=question_text
            )
        return prompt