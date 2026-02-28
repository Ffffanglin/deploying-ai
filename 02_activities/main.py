from services.api_service import get_joke
from services.semantic_service import add_document, query_document
from services.custom_service import chat_response, client as custom_client

history = []

print("Welcome to the AI Chat System!")
print("Type 'exit' to end the conversation.")
print("Available commands: add_document, search, get_joke, chat")

while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() == "exit":
        print("Ending conversation. Goodbye!")
        break
    elif user_input.lower() == "get_joke":
        reply = get_joke()
    elif user_input.lower() == "add_document":
        doc_id = input("Enter document ID: ").strip()
        text = input("Enter document text: ").strip()
        source = input("Enter source (optional): ").strip() or "unknown"
        reply = add_document(doc_id, text, source)
    elif user_input.lower() == "search":
        query_text = input("Enter your query: ").strip()
        search_results = query_document(query_text, n_results=3)
        reply = f"Search results: {search_results}"
    else:
        # Default: chat service
        reply = chat_response(custom_client, user_input, history)
        history.append({"user": user_input, "assistant": reply})

    print("Assistant:", reply)