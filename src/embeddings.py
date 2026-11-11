
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL


model = SentenceTransformer(EMBEDDING_MODEL)


def generate_embeddings(chunks):

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings
