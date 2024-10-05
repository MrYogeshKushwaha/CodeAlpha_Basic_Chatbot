# ChatGPT-Like Chatbot

A simple text-based chatbot application built using Python's `Tkinter` and `spaCy`. This chatbot can engage in conversations and respond to various common questions and queries, making it a great starting point for understanding natural language processing and GUI development.

## Features

- **Conversational Interface**: A user-friendly GUI that simulates a chat application.
- **Daily Life Questions**: The chatbot can respond to common inquiries, including:
  - Greetings
  - Weather inquiries
  - Current time
  - Favorite things
  - Simple factual questions
- **Real-time Interaction**: Users can type their messages and receive responses instantly.

## Requirements

Before running the chatbot, ensure you have the following installed:

- Python 3.x
- `spaCy` library
- `Tkinter` library (comes pre-installed with Python)

### Install spaCy and the English model

You can install `spaCy` and download the English language model with the following commands:

```bash
pip install spacy
python -m spacy download en_core_web_sm
