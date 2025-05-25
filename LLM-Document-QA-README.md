
# 📄 LLM Document QA System

This project is a document-based Question Answering (QA) system powered by Large Language Models (LLMs). It allows users to upload PDF documents and ask natural language questions based on the document content. The system uses text chunking, embeddings, and retrieval-augmented generation to produce accurate answers.

---

## 📁 Project Structure

```
LLM-Document-QA/
├── requirements.txt       # Project dependencies
├── config.py              # Configuration settings
├── pdf_reader.py          # PDF parsing and text extraction
├── chunker.py             # Text chunking logic
├── embedder.py            # Text to vector embedding
├── qa_engine.py           # Core QA engine using LLMs
├── main.py                # Optional CLI or backend runner
└── ui_streamlit.py        # Streamlit web UI
```

---

## 🔍 Module Descriptions

### `requirements.txt`
Lists all required Python packages such as:
- `streamlit` – for the web UI
- `PyPDF2` or `pdfplumber` – for reading PDFs
- `langchain`, `openai`, `sentence-transformers` – for LLM and embedding
- `faiss-cpu` or `chromadb` – for vector search

---

### `config.py`
Stores project settings:
- API keys
- Embedding model info
- Chunking size
- Retrieval parameters like `top_k`

---

### `pdf_reader.py`
Handles:
- Reading PDF files
- Extracting plain text
- Handling multi-page documents

---

### `chunker.py`
Splits long document text into smaller overlapping or non-overlapping chunks to:
- Fit the context window of LLMs
- Preserve information continuity

---

### `embedder.py`
Embeds chunks into vector representations using:
- Sentence Transformers
- OpenAI Embeddings
- Other LLM-compatible embedding models

---

### `qa_engine.py`
The core logic:
- Accepts user question
- Retrieves top relevant document chunks via similarity search
- Sends query + context to LLM for response

---

### `main.py`
May be used to:
- Run processing without UI
- Index or debug the pipeline

---

### `ui_streamlit.py`
A web interface using Streamlit to:
- Upload documents
- Enter user questions
- Display model-generated answers

---

## 🧪 How It Works (Workflow)

1. **Upload PDF** → Extract text via `pdf_reader.py`
2. **Chunk Document** → `chunker.py` splits text
3. **Vector Embedding** → `embedder.py` generates vectors
4. **Store/Search Vectors** → Similarity search (likely via FAISS/ChromaDB)
5. **Answer Query** → `qa_engine.py` builds context and uses LLM to answer
6. **Interact via UI** → `ui_streamlit.py` provides interface

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone <repo-url>
cd LLM-Document-QA
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set API Keys
Edit `config.py` or use environment variables to configure your OpenAI/embedding model API keys.

### 5. Launch the App
```bash
streamlit run ui_streamlit.py
```

Then open your browser to `http://localhost:8501`.

---

## ✅ Features
- Upload any PDF document
- Ask questions based on document content
- LLM-powered responses using document context
- Modular, extendable Python codebase

---

## 📌 Requirements
- Python 3.8+
- OpenAI API key (or compatible LLM/embedding provider)
- Internet connection (for API-based embeddings/LLMs)

---

## 🛠️ To Do
- Add persistent vector storage (e.g., FAISS/Chroma)
- Enhance UI for multi-doc support
- Add authentication for API keys

