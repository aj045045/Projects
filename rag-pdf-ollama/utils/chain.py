# utils/chain.py

from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from config.env import env_settings


def create_qa_chain(vectorstore):
    llm = OllamaLLM(model=env_settings.OLLAMA_MODEL)
    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    )
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain
