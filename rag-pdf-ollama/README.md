# 🧠 PDF Q&A with LangChain + Ollama

This is a **Retrieval-Augmented Generation (RAG)** app that allows you to upload a PDF and ask questions about its content. Powered by **LangChain**, **Ollama**, **FAISS**, and a simple **Streamlit** UI.

## 📁 Project Structure

```
.
├── assets/                   # Images, logos, or static files
├── config/
│   └── env.py                # Environment and model config
├── docs/                    # Documentation and demo images
├── main.py                  # Streamlit app entry point
└── utils/
    └── chain.py
    └── embedding.py

```

---

## ⚙️ Features

- 📄 Upload any PDF file
- 🧠 Extract context and answer questions using RAG
- 🔗 LangChain + FAISS for document retrieval
- 🦙 Ollama for running local LLMs (like LLaMA3, Mistral, etc.)
- 🖥️ Streamlit UI with markdown answers and debug tools

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/aj045045/project.git
cd project/pdf-rag-ollama
```

### 2. Install Dependencies

```bash
pip install -q langchain-ollama langchain-community langchain streamlit pypdf pydantic-settings
```

### 3. Start Ollama & Pull a Model

> Make sure [Ollama](https://ollama.com) is installed and running.

```bash
ollama pull mistral:7b nomic-embed-text
```

You can replace `llama3` with other supported models like `mistral`, `gemma`, etc.

### 4. Run the App

```bash
streamlit run main.py
```

---

## 🧠 Example Use Cases

- 📚 Academic paper summarization
- 💼 Resume screening and analysis
- 📝 Legal and business document Q\&A
- 🤖 Building intelligent document chatbots

---

## 🛠 Tech Stack

| Tool      | Purpose                         |
| --------- | ------------------------------- |
| Streamlit | UI Framework                    |
| LangChain | RAG & LLM chaining              |
| Ollama    | Local LLM inference             |
| FAISS     | Vector similarity search        |
| PyPDF     | PDF parsing and text extraction |

---

## 🧪 Sample Output

Question: What skills are highlighted in the document?

Answer:

1. **Technical Skills**: Data Engineering, ML Ops, Full-Stack Dev
2. **Libraries**: Kafka, Airflow, TensorFlow, Dask
3. **Soft Skills**: Leadership, Critical Thinking, Collaboration

---

## ✅ Features

- **Support multi-PDF uploads** – Upload and process multiple PDFs at once.
- **Add chunk preview or highlighting** – See relevant chunks used for answering the question.
- **Include citation/source documents** – Source document metadata is shown with the answer.

---

## 👤 Author

**Ansh Yadav**
→ [GitHub](https://github.com/aj045045) | [LinkedIn](https://www.linkedin.com/anshyadav045)
