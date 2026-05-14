from langchain.memory import ConversationBufferMemory

class ChatMemory:
    def __init__(self):
        self.memory = ConversationBufferMemory(
            memory_key="history",
            return_messages=True,
            k=15 
        )

    def get_history(self):
        return self.memory.chat_memory.messages

    def add_user(self, text: str):
        self.memory.chat_memory.add_user_message(text)

    def add_ai(self, text: str):
        self.memory.chat_memory.add_ai_message(text)

    def clear(self):
        self.memory.clear()