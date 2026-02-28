# AI Chat System - Assignment 2
Overview

This project implements an AI chat system with a conversational interface. The system integrates three distinct services:

API Service – fetches and rephrases content from a public API.
Semantic Search Service – allows users to query documents using embeddings and ChromaDB.
Custom Chat Service – provides a conversational AI assistant with memory and guardrails.

The interface is terminal-based, maintaining conversation history to enable context-aware responses. Guardrails prevent the assistant from responding to restricted topics.

## Services
### Service 1: API Service (api_service.py)
Fetches a random joke from the Official Joke API.
Rephrases the joke in a friendly, conversational tone.
Function: get_joke() -> str

### Service 2: Semantic Search Service (semantic_service.py)
Uses ChromaDB to store documents with embeddings.
Functions:
add_document(doc_id: str, text: str, source: str = "unknown") – adds a document with embedding.
query_document(query_text: str, n_results: int = 1) – performs a semantic search.

### Service 3: Custom Chat Service (custom_service.py)
Uses OpenAI GPT-4o-mini for chat responses.
Maintains conversation memory in history.
Implements guardrails to block restricted topics:
Cats or dogs
Horoscopes or Zodiac Signs
Taylor Swift
Function: chat_response(client, user_input, conversation_history) -> str

## User Interface (main.py)
Terminal-based chat client.
Available commands:
get_joke – calls API Service
add_document – adds a new document to ChromaDB
search – queries documents
chat – interacts with the Custom Chat Service
