"""
AI Educational RAG Assistant
Basic Retrieval-Augmented Generation pipeline.
"""

from pathlib import Path
from config import DATA_PATH, TOP_K_RESULTS


# Load educational resources
def load_documents(file_path):
    """Read the educational knowledge base."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")


# Simple keyword-based retrieval
def retrieve_context(query, document):
    """Retrieve relevant sections based on query keywords."""
    query_words = set(query.lower().split())

    sections = document.split("\n## ")

    scored_sections = []

    for section in sections:
        section_lower = section.lower()
        score = sum(word in section_lower for word in query_words)

        if score > 0:
            scored_sections.append((score, section))

    scored_sections.sort(reverse=True, key=lambda item: item[0])

    return "\n\n".join(
        section for _, section in scored_sections[:TOP_K_RESULTS]
    )


# Generate a response using retrieved context
def generate_response(query, context):
    """Create a simple context-based response."""
    if not context:
        return "No relevant educational information was found."

    return (
        "Based on the educational resources:\n\n"
        f"{context}\n\n"
        f"Question: {query}"
    )


# Complete RAG pipeline
def rag_pipeline(query):
    """Run retrieval and response generation."""
    data_path = Path(__file__).parent.parent / DATA_PATH

    document = load_documents(data_path)
    context = retrieve_context(query, document)

    return generate_response(query, context)


if __name__ == "__main__":
    question = input("Ask an educational question: ")
    answer = rag_pipeline(question)

    print("\nAnswer:")
    print(answer)
