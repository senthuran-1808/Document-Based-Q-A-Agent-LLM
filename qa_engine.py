from transformers import pipeline
import numpy as np
import config

def get_top_chunks(query, embed_model, faiss_index, stored_chunks, k=3):
    query_vec = embed_model.encode([query])
    _, indices = faiss_index.search(query_vec, k)
    results = [stored_chunks[i] for i in indices[0]]
    return "\n".join(results)

def generate_answer(question, context):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    generator = pipeline("text2text-generation", model=config.LLM_MODEL_NAME)
    response = generator(prompt, max_length=256, do_sample=False)
    return response[0]['generated_text']