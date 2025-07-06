import sys
import os
import time
import streamlit as st

# Add the parent directory to sys.path to import local modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llm.agents import run_diagnosis_crew
from llm.model import predict_disease_tf

# Configure Streamlit page
st.set_page_config(
    page_title="Plant Disease Advisor",
    layout="wide",
    page_icon="🌿"
)

# --- Sidebar Info ---
with st.sidebar:
    st.title("🧠 About This App")
    st.markdown("""
    This **AI-powered plant disease advisor** helps farmers, researchers, and hobbyists detect diseases in crops through simple image uploads. 
    
    Built with:
    - 🧠 TensorFlow for disease prediction
    - 🕸️ Kafka for real-time streaming
    - 🧬 LangChain + Ollama for AI diagnosis
    - 🛠️ MLflow for tracking performance
    - 🤖 CrewAI agents for expert reasoning

    📚 Dataset: [PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease)

    🔗 Source: [Kaggle Notebook](https://www.kaggle.com/code/aj045045/plant-predication)
    """)

# --- App Title and Subtitle ---
st.title("🌿 Plant Disease Diagnosis Assistant")
st.markdown("""
Upload a high-quality image of a **plant leaf**, and let our AI detect any potential diseases and provide expert suggestions for treatment.

This tool is designed to assist farmers, researchers, and agritech enthusiasts in early disease detection and management.
""")

# --- Features Section ---
with st.expander("🔍 What Can This Tool Do?"):
    st.markdown("""
    ✅ Detect diseases from plant leaf images  
    ✅ Generate AI-guided solutions using natural language  
    ✅ Process images in real-time  
    ✅ Display diagnosis reports powered by local LLMs  
    ✅ Track model predictions for experimentation  

    Supported diseases include:
    - 🍎 Apple Scab
    - 🌽 Corn Rust
    - 🍇 Grape Black Rot
    - 🥔 Potato Early Blight
    - 🍅 Tomato Mosaic Virus
    """)

# --- File uploader ---
uploaded_file = st.file_uploader("📤 Upload a plant leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="🖼️ Uploaded Leaf Image", use_container_width=False)

    with st.spinner("🔍 Analyzing image and predicting disease..."):
        time.sleep(5)  # Simulate processing delay
        prediction = predict_disease_tf(uploaded_file)

    prediction_clean = prediction.replace("_", " ")
    st.success(f"🩺 **Predicted Disease:** {prediction_clean}")

    with st.spinner("🧠 Engaging expert agents for a comprehensive diagnosis..."):
        output = run_diagnosis_crew(prediction)

    st.subheader("📋 AI Diagnosis Report")
    st.markdown(output, unsafe_allow_html=True)
else:
    st.warning("📎 Please upload an image of a plant leaf to begin diagnosis.")

# --- Footer ---
st.markdown("---")
st.markdown("""
🧠 **How it works:**

1. You upload a plant leaf image.
2. A deep learning model built with TensorFlow analyzes the image.
3. The system predicts the disease and engages AI agents (via CrewAI) for deeper insights.
4. You receive a diagnosis and recommendations, all powered by local LLMs and LangChain pipelines.

---

💬 For feedback, feature requests, or contributions, please reach out or check the [GitHub repo](https://github.com/aj045045/project).
""")
