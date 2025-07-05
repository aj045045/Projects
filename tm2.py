from langchain_community.llms.ollama import Ollama

llm = Ollama(model="mistral:7b")
response = llm("What is Tomato Leaf Curl Virus?")
print(response)
