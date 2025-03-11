from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI


class ChatBotChain:
    def __init__(self, model_name="gpt-4", temperature=0.7):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        prompt = PromptTemplate(input_variables=["query"], template="Answer the following: {query}")
        self.chain = LLMChain(llm=self.llm, prompt=prompt)

    def execute(self, query):
        return self.chain.run(query)
