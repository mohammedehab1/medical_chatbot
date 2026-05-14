from langchain.schema import SystemMessage, HumanMessage
from stores.llm.templates.template_parser import TemplateParser

class ChatEngine:
    def __init__(self, llm, memory):
        self.llm = llm
        self.memory = memory
        self.parser = TemplateParser(default_language="ar")

    def chat(self, user_input: str):
        lang = self.parser.detect_language(user_input)
        self.parser.set_language(lang)
        system_prompt = self.parser.get("prompts", "SYSTEM_PROMPT")

        history = self.memory.get_history()

        messages = [SystemMessage(content=system_prompt)] + history + [
            HumanMessage(content=user_input)
        ]

        response = self.llm.invoke(messages)
        answer = response.content.strip()

        self.memory.add_user(user_input)
        self.memory.add_ai(answer)

        return answer