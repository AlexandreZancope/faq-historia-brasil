import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # nova importação

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def load_llm():
    return ChatOpenAI(temperature=0.5, model="gpt-3.5-turbo")  # ou "gpt-4"