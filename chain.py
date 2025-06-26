from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from utils import load_llm

def build_chain():
    prompt_template = PromptTemplate(
        input_variables=["question"],
        template="""
Você é um assistente educacional especializado em História do Brasil.
Responda à pergunta de forma clara, objetiva e didática.

Pergunta: {question}
Resposta:"""
    )
    
    llm = load_llm()
    return LLMChain(prompt=prompt_template, llm=llm)