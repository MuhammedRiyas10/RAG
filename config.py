
# ==============================
# DOCUMENT CONFIGURATION
# ==============================

DATA_PATH = "data/documents"

# ==============================
# CHUNK CONFIGURATION
# ==============================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# ==============================
# EMBEDDING CONFIGURATION
# ==============================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==============================
# VECTOR DATABASE CONFIGURATION
# ==============================

FAISS_INDEX_PATH = "vectorstore/faiss_index.bin"
CHUNKS_PATH = "vectorstore/chunks.pkl"

# ==============================
# RETRIEVAL CONFIGURATION
# ==============================

TOP_K = 3

# ==============================
# LLM CONFIGURATION
# ==============================

GROQ_MODEL = "openai/gpt-oss-120b"
