from crewai import Agent, Task, Crew

# Agent: Disease Classifier
classifier_agent = Agent(
    role="Plant Disease Classifier",
    goal="Classify plant disease from an image",
    backstory="An AI trained to detect plant diseases using deep learning.",
    tools=[],
    allow_delegation=False
)

# Agent: Solution Expert
solution_agent = Agent(
    role="Plant Pathology Expert",
    goal="Provide treatment and prevention for plant diseases",
    backstory="An AI expert in agriculture and plant pathology.",
    tools=[],
    allow_delegation=False
)

# Task 1: Classification
classification_task = Task(
    description="Analyze the input image and identify the plant disease.",
    expected_output="The name of the plant disease.",
    agent=classifier_agent
)

# Task 2: Solution
solution_task = Task(
    description="Based on the disease name, generate a solution including treatment and prevention.",
    expected_output="Detailed treatment plan and prevention strategy.",
    agent=solution_agent
)

# Crew
crew = Crew(
    agents=[classifier_agent, solution_agent],
    tasks=[classification_task, solution_task],
    verbose=True
)

# Simulated flow (replace with actual image input/output integration)
def run_pipeline(image_path):
    disease_name = predict_disease(image_path)
    solution = get_solution(disease_name)
    
    print(f"[DISEASE] {disease_name}")
    print(f"[SOLUTION]\n{solution}")
