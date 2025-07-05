from langchain_ollama import OllamaLLM
from crewai import Agent, Task, Crew

llm = OllamaLLM(model="mistral:7b")


# 1. Disease Explanation Agent
disease_explainer = Agent(
    role="Plant Pathology Expert",
    goal="Explain the disease in a way farmers understand",
    backstory="A botanist with years of experience in plant disease diagnosis.",
    llm=llm
)

# 2. Treatment Advisor Agent
treatment_advisor = Agent(
    role="Agricultural Consultant",
    goal="Provide best treatments and preventions for the disease",
    backstory="An agriculture expert who helps farmers combat plant issues.",
    llm=llm
)


# Suppose your DL model predicts 'Tomato Leaf Curl Virus'
predicted_disease = "Tomato Leaf Curl Virus"

task1 = Task(
    description=f"Explain the plant disease '{predicted_disease}' to a farmer in simple terms.",
    expected_output="A detailed but simple explanation of the disease and its effects.",
    agent=disease_explainer
)

task2 = Task(
    description=f"Suggest organic and chemical treatment methods for '{predicted_disease}', including prevention tips.",
    expected_output="Treatment and prevention plan suitable for tropical regions.",
    agent=treatment_advisor
)


crew = Crew(
    agents=[disease_explainer, treatment_advisor],
    tasks=[task1, task2],
    verbose=True  # to see what's happening
)

results = crew.kickoff()
print(results)


# pip install langchain langchain-community crewai ollama
