import requests

def get_joke():
    """Fetch a random joke from a public API and rephrase it."""
    try:
        res = requests.get("https://official-joke-api.appspot.com/random_joke")
        res.raise_for_status()
        data = res.json()
        # Rephrase joke in a conversational tone
        joke = f"Here's a joke for you: {data['setup']} ... {data['punchline']} 😄"
        return joke
    except Exception as e:
        return f"Sorry, I couldn't fetch a joke. Error: {e}"

# --- CALL THE FUNCTION ---
if __name__ == "__main__":
    joke = get_joke()
    print(joke)