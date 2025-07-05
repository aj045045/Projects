from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="llama3")

def get_solution(disease_name):
    template = """
    The plant disease detected is: {disease}.
    Please provide:
    - A brief explanation of the disease.
    - Treatment options.
    - Prevention strategies.
    """
    prompt = PromptTemplate.from_template(template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"disease": disease_name})
