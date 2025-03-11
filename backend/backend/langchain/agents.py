from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool

class ChatBotAgent:
    def __init__(self, model_name="gpt-4", temperature=0.7):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.memory = ConversationBufferMemory(memory_key="chat_history")
        self.tools = [Tool(name="analyze_data", func=lambda x: f"Analyzing {x}")]
        self.agent = initialize_agent(self.tools, self.llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, memory=self.memory)

    def chat(self, query):
        return self.agent.run(query)
