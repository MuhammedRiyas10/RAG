
from src.retriver import retrieve_documents
from src.llm import generate_response


def rag_pipeline(query):

    print("\nSearching relevant documents...")

    # Step 1: Retrieve relevant chunks
    retrieved_chunks = retrieve_documents(query)

    if not retrieved_chunks:
        return {
            "answer": "No relevant information found.",
            "sources": []
        }

    # Step 2: Construct context
    context = "\n\n".join(
        [item["text"] for item in retrieved_chunks]
    )

    print("Relevant documents retrieved.")

    # Step 3: Generate response using Groq
    print("Generating answer...")

    answer = generate_response(
        query,
        context
    )

    return {
        "answer": answer,
        "sources": retrieved_chunks
    }
