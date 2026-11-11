
from src.rag import rag_pipeline


def main():

    print("=" * 50)
    print("          BASIC RAG APPLICATION")
    print("=" * 50)

    while True:

        query = input("\nEnter your question: ")

        if query.lower().strip() in ["exit", "quit"]:

            print("Exiting RAG application...")
            break

        if not query.strip():
            print("Please enter a valid question.")
            continue

        try:

            result = rag_pipeline(query)

            print("\n" + "=" * 50)
            print("ANSWER")
            print("=" * 50)

            print(result["answer"])

            print("\n" + "=" * 50)
            print("RETRIEVED SOURCES")
            print("=" * 50)

            for i, source in enumerate(
                result["sources"], start=1
            ):

                print(f"\nChunk {i}")
                print("Similarity:", source["score"])
                print("Content:", source["text"])

        except Exception as e:

            print("Error:", e)


if __name__ == "__main__":
    main()
