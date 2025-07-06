# from crewai import Agent, Task, Crew, LLM

# def run_diagnosis_crew(predicted_disease: str):
#     try:
#         # Setup LLM
#         llm = LLM(model="ollama/mistral:7b", base_url="http://localhost:11434")

#         # Define the only Agent: Plant Pathology Expert
#         disease_explainer = Agent(
#             role="Plant Pathology Expert",
#             goal="Explain the disease in a way farmers understand",
#             backstory="A botanist with years of experience in plant disease diagnosis. You are great at explaining scientific concepts in clear, simple, and visually structured Markdown format.",
#             llm=llm
#         )

#         # Define the only Task
#         task = Task(
#             description=(
#                 "Write a detailed, farmer-friendly explanation of the plant disease '{{predicted_disease}}'. "
#                 "Structure the output using Markdown formatting. Include sections like title, symptoms, causes, "
#                 "environmental triggers, and prevention or treatment tips. Use bullet points, bold text, and headings "
#                 "where appropriate."
#             ),
#             expected_output=(
#                 "A well-formatted Markdown explanation including:\n"
#                 "- Disease title with emoji\n"
#                 "- Simple explanation\n"
#                 "- Symptoms list\n"
#                 "- Causes\n"
#                 "- When it usually occurs\n"
#                 "- Prevention and treatment steps\n"
#             ),
#             agent=disease_explainer
#         )

#         # Create and run the Crew
#         crew = Crew(
#             agents=[disease_explainer],
#             tasks=[task],
#             verbose=True
#         )

#         # Run the task
#         response = crew.kickoff(inputs={"predicted_disease": predicted_disease})

#         # Return Markdown-formatted explanation
#         return f"""### 🧪 Disease Explanation\n\n{response}"""

#     except Exception as e:
#         return f"❌ ERROR during diagnosis execution:\n{str(e)}"


import streamlit as st
from crewai import Agent, Task, Crew, LLM

@st.cache_resource
def get_disease_explainer():
    llm = LLM(model="ollama/mistral:7b", base_url="http://localhost:11434")

    agent = Agent(
        role="Plant Pathology Expert",
        goal="Explain the disease in a way farmers understand",
        backstory="A botanist with years of experience...",
        llm=llm
    )

    task = Task(
        description=(
            "Write a detailed, farmer-friendly explanation of the plant disease '{{predicted_disease}}'..."
        ),
        expected_output=(
            "A well-formatted Markdown explanation including:\n"
            "- Disease title with emoji\n"
            "- Simple explanation\n"
            "- Symptoms list\n"
            "- Causes\n"
            "- When it usually occurs\n"
            "- Prevention and treatment steps\n"
        ),
        agent=agent
    )

    return agent, task

@st.cache_resource
def get_crew():
    agent, task = get_disease_explainer()
    return Crew(agents=[agent], tasks=[task], verbose=False)

def run_diagnosis_crew(predicted_disease: str):
    try:
        crew = get_crew()
        response = crew.kickoff(inputs={"predicted_disease": predicted_disease})

        # Wrap in a styled div
        return f"""
        <div style="background-color:#e6ffe6; padding:20px; border-radius:10px;">
            <h3>🧪 Disease Explanation</h3>
            {response}
        </div>
        """
    except Exception as e:
        return f"<div style='background-color:#ffe6e6; padding:20px; border-radius:10px;'>❌ ERROR: {str(e)}</div>"
