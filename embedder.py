import faiss
from sentence_transformers import SentenceTransformer
import config

def embed_chunks(chunks):
    model = SentenceTransformer(config.EMBED_MODEL_NAME)
    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)

    return index, embeddings, chunks, model