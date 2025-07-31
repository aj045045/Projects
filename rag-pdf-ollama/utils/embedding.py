# utils/embedding.py

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from config.env import EnvSettings

env = EnvSettings()


def process_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)


def embed_docs(chunks):
    embeddings = OllamaEmbeddings(model=env.OLLAMA_EMBEDDING_MODEL)
    return FAISS.from_documents(chunks, embeddings)
