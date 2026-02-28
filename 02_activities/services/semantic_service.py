import os
from openai import OpenAI
import chromadb
from dotenv import load_dotenv
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent
secrets_path = SCRIPT_DIR / "../../05_src/.secrets"

load_dotenv(secrets_path.resolve())

api_gateway_key = os.getenv("API_GATEWAY_KEY")
if not api_gateway_key:
    raise ValueError(
        f"API_GATEWAY_KEY not found. Check your .secrets file at {secrets_path.resolve()}"
    )


client = OpenAI(
    base_url="https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1",
    api_key="any value",
    default_headers={"x-api-key": api_gateway_key}
)

response = client.responses.create(
    model="gpt-4o-mini",
    input="Hello world!"
)

print("Model response:", response.output_text)

chroma_client = chromadb.Client()
collection_name = "semantic_collection"

try:
    collection = chroma_client.get_collection(name=collection_name)
except:
    collection = chroma_client.create_collection(name=collection_name)


def add_document(doc_id: str, text: str, source: str = "unknown"):
    """Add a document to Chroma with embedding."""
    
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    embedding = response.data[0].embedding

    collection.add(
        documents=[text],
        metadatas=[{"source": source}],
        ids=[doc_id],
        embeddings=[embedding]  
    )
    print(f"Document {doc_id} added.")

# Helper function: query documents
def query_document(query_text: str, n_results: int = 1):
    """Perform semantic search."""
    # Embed query
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query_text
    )
    query_embedding = response.data[0].embedding

    # Query Chroma
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results

# Example usage
if __name__ == "__main__":
    # Add a document
    add_document("doc1", "Hello world! This is a test document.", source="test_source")

    # Query it
    query_text = "test"
    search_results = query_document(query_text, n_results=1)
    print("Search results:", search_results)