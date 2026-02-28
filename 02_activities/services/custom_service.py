import os
from openai import OpenAI
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

def chat_response(user_input: str, conversation_history: list):
    """Generate a chat response while enforcing guardrails."""
    restricted_topics = ["cats", "dogs", "horoscope", "zodiac", "taylor swift"]
    if any(topic in user_input.lower() for topic in restricted_topics):
        return "I'm sorry, I can't answer questions about that topic."

    # Build messages format for OpenAI Responses API
    messages = [{"role": "system", "content": "You are a friendly, witty AI assistant."}]
    for h in conversation_history:
        messages.append({"role": "user", "content": h["user"]})
        messages.append({"role": "assistant", "content": h["assistant"]})
    messages.append({"role": "user", "content": user_input})

    # --- Call OpenAI Responses API ---
    response = client.responses.create(
        model="gpt-4o-mini",
        input=messages
    )
    return response.output_text

if __name__ == "__main__":
    history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat...")
            break
        reply = chat_response(user_input, history)
        print("Assistant:", reply)
        history.append({"user": user_input, "assistant": reply})