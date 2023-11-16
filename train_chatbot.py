import nltk
from nltk.chat.util import Chat, reflections

# Download the NLTK data needed for the chat module
nltk.download('punkt')
nltk.download('chat80')

# Define custom reflections for the chat
my_reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
}

# Define patterns for the chatbot to recognize
my_patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ["I'm doing well, thank you! How about you?"]),
    (r'(.*) your name (.*)', ["I'm a chatbot.", "You can call me ChatGPT."]),
    (r'(.*) (weather|temperature) (.*)', ["I'm sorry, I don't have real-time weather information."]),
    (r'(.*) (good|bad) (.*)', ["I'm just a computer program, so I don't have feelings, but I'm here to help!"]),
    (r'quit|bye', ["Goodbye! Have a great day."]),
]

# Create a chatbot using NLTK's Chat class
my_chatbot = Chat(my_patterns, reflections=my_reflections)

# Function to start and run the chat
def start_chat():
    print("Hello! I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day.")
            break
        response = my_chatbot.respond(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    start_chat()
