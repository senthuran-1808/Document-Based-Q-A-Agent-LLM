import streamlit as st
from main import run_qa_pipeline

st.title("Document Based Q&A Agent-LLM")
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    question = st.text_input("Ask a question from this document:")

    if st.button("Get Answer") and question:
        with st.spinner("Processing..."):
            answer = run_qa_pipeline("uploaded.pdf", question)
            st.markdown(f"**Answer:** {answer}")