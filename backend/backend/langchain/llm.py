from langchain.chat_models import ChatOpenAI

class LLM:
    """"We can use GPT, Claude any best llm"""
    def __init__(self, model_name="gpt-4", temperature=0.7):
        self.model = ChatOpenAI(model_name=model_name, temperature=temperature)
    
    def query(self, text):
        response = self.model.invoke(text)
        return response.content
