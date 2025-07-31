import streamlit as st
import tempfile
from utils.embedding import process_pdf, embed_docs
from utils.chain import create_qa_chain

st.set_page_config(page_title="PDF Q&A with RAG 🔍", layout="centered")

st.title("📄 RAG-based PDF Question Answering App")
st.markdown(
    "Ask questions from your uploaded PDF using **Ollama + LangChain** powered Retrieval-Augmented Generation."
)

# Upload PDF
uploaded_file = st.file_uploader("📎 Upload your PDF file", type="pdf")
question = st.text_input("❓ Enter your question based on the PDF content:")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        pdf_path = temp_pdf.name

    with st.spinner("🔄 Processing and indexing your PDF..."):
        documents = process_pdf(pdf_path)
        vector_store = embed_docs(documents)
        qa_chain = create_qa_chain(vector_store)
        st.success("✅ PDF successfully processed and embedded!")

    if question:
        with st.spinner("Generating answer..."):
            response = qa_chain.invoke({"query": question})
            answer = response.get("result", "⚠️ No result returned.")

            st.markdown("### 🧠 Answer:")
            st.markdown(answer, unsafe_allow_html=False)
