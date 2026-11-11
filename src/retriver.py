
import faiss
import pickle
import numpy as np

from config import (
    FAISS_INDEX_PATH,
    CHUNKS_PATH,
    TOP_K
)

from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL


# Load embedding model
model = SentenceTransformer(EMBEDDING_MODEL)


def load_vector_store():

    # Load FAISS index
    index = faiss.read_index(FAISS_INDEX_PATH)

    # Load original chunks
    with open(CHUNKS_PATH, "rb") as file:
        chunks = pickle.load(file)

    return index, chunks


def retrieve_documents(query):

    # Load vector database
    index, chunks = load_vector_store()

    # Convert query into embedding
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    query_embedding = np.asarray(
        query_embedding,
        dtype="float32"
    )

    # Similarity search
    scores, indices = index.search(
        query_embedding,
        min(TOP_K, index.ntotal)
    )

    retrieved_chunks = []

    # Fetch original text using FAISS IDs
    for score, idx in zip(scores[0], indices[0]):

        if idx == -1:
            continue

        retrieved_chunks.append({
            "text": chunks[idx],
            "score": float(score)
        })

    return retrieved_chunks
