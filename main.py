from pdf_reader import read_pdf
from chunker import split_text
from embedder import embed_chunks
from qa_engine import get_top_chunks, generate_answer

def run_qa_pipeline(pdf_path, question):
    raw_text = read_pdf(pdf_path)
    chunks = split_text(raw_text)

    faiss_index, embeddings, stored_chunks, embed_model = embed_chunks(chunks)

    context = get_top_chunks(question, embed_model, faiss_index, stored_chunks)
    answer = generate_answer(question, context)

    return answer