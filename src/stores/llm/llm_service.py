from langchain_groq import ChatGroq
from helpers.config import settings

from stores.llm.memory.chat_memory import ChatMemory
from stores.llm.chat_engine import ChatEngine


class LLMService:
    def __init__(self):
        self.llm = ChatGroq(
            model=settings.LLM_MODEL,
            temperature=settings.TEMPERATURE,
            max_retries=settings.MAX_RETRIES,
            groq_api_key=settings.GROQ_API_KEY
        )

        self.memory = ChatMemory()

        self.engine = ChatEngine(self.llm, self.memory)

    def chat(self, user_input: str):
        return self.engine.chat(user_input)