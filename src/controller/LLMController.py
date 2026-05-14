from stores.llm import LLMService

class LLMController:
    def __init__(self):
        self.llm_service = LLMService()

    def chat(self, user_input: str) -> str:
        response = self.llm_service.chat(user_input)
        return response