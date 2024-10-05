import spacy
import tkinter as tk
from tkinter import scrolledtext
import random
import datetime

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define some sample responses to different types of queries
RESPONSES = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! How can I help?", "Hey! What's on your mind?"],
    "how_are_you": ["I'm a chatbot, so I don't have feelings, but I'm here to help you!", "I'm functioning as expected! How about you?"],
    "name": ["I'm Chatbot, your virtual assistant!", "You can call me Chatbot. What can I do for you?"],
    "help": ["I'm here to answer your questions. You can ask me about anything simple or just chat!", "How can I assist you today?"],
    "farewell": ["Goodbye! Have a great day!", "Farewell! It was nice chatting with you!", "Take care! See you next time!"],
    "weather": ["I don't have real-time weather data, but it looks like a great day to be productive!", "I can't provide weather updates, but I hope it's sunny wherever you are!"],
    "time": [f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}", "It's time for you to shine!"],
    "favorite_color": ["I love blue, just like the sky!", "I like green, it reminds me of growth and nature."],
    "age": ["I was created recently, so you can say I'm quite young!", "Age is just a number! But I'm as old as the code that created me."],
    "unknown": ["I'm sorry, I didn't quite understand that. Could you try asking something else?", "Hmm, I'm not sure I understand. Could you clarify?"],
}

# Helper function to identify the intent of the user
def get_intent(user_input):
    doc = nlp(user_input.lower())
    
    # Check for common intents using keywords and named entities
    if any(token.lemma_ in ["hello", "hi", "hey", "greetings"] for token in doc):
        return "greeting"
    elif "how" in [token.text for token in doc] and "you" in [token.text for token in doc]:
        return "how_are_you"
    elif any(token.lemma_ in ["name", "who", "what"] for token in doc) and "you" in [token.text for token in doc]:
        return "name"
    elif any(token.lemma_ in ["help", "assist"] for token in doc):
        return "help"
    elif any(token.lemma_ in ["bye", "goodbye", "farewell", "see you"] for token in doc):
        return "farewell"
    elif any(token.lemma_ in ["weather", "rain", "sunny"] for token in doc):
        return "weather"
    elif any(token.lemma_ in ["time", "clock", "hour"] for token in doc):
        return "time"
    elif any(token.lemma_ in ["color", "favourite", "favorite"] for token in doc) and "your" in [token.text for token in doc]:
        return "favorite_color"
    elif any(token.lemma_ in ["age", "old"] for token in doc) and "you" in [token.text for token in doc]:
        return "age"
    else:
        return "unknown"

# Function to generate a response
def generate_response(user_input):
    intent = get_intent(user_input)
    return random.choice(RESPONSES[intent])

# Function to handle sending a message
def send_message():
    user_input = user_input_entry.get()
    if user_input.strip():  # Only process non-empty inputs
        # Display user's message in the conversation window
        chat_window.configure(state='normal')
        chat_window.insert(tk.END, "You: " + user_input + '\n', 'user')
        
        # Get the chatbot response
        response = generate_response(user_input)
        chat_window.insert(tk.END, "Chatbot: " + response + '\n\n', 'bot')
        
        # Scroll to the end of the text area
        chat_window.yview(tk.END)
        chat_window.configure(state='disabled')

        # Clear the input entry field
        user_input_entry.delete(0, tk.END)

# Set up the GUI window
root = tk.Tk()
root.title("Jarvis Chatbot")
root.geometry("600x600")
root.resizable(False, False)

# Chat conversation area (scrollable)
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Tag configurations for user and bot styling
chat_window.tag_config('user', foreground='blue', font=("Arial", 12, "bold"))
chat_window.tag_config('bot', foreground='green', font=("Arial", 12))

# Frame to hold the user input and send button
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, padx=10, pady=10)

# User input entry field
user_input_entry = tk.Entry(input_frame, font=('Arial', 14), width=50)
user_input_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

# Send button
send_button = tk.Button(input_frame, text="Send", command=send_message, width=10, height=1, font=('Arial', 12))
send_button.pack(side=tk.RIGHT, padx=5)

# Allow pressing 'Enter' to send message
root.bind('<Return>', lambda event: send_message())

# Start the Tkinter main loop
root.mainloop()
