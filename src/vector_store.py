
import faiss
import numpy as np
import pickle
import os

from config import FAISS_INDEX_PATH, CHUNKS_PATH


def create_vector_store(embeddings, chunks):

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatIP(dimension)

    # Add embeddings
    index.add(embeddings)

    # Create storage directory
    os.makedirs("vectorstore", exist_ok=True)

    # Save FAISS index
    faiss.write_index(index, FAISS_INDEX_PATH)

    # Save original text chunks
    with open(CHUNKS_PATH, "wb") as file:

        pickle.dump(chunks, file)

    print("Vector store created successfully!")
