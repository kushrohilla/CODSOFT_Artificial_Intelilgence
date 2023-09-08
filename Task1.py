import re
import random

# Define a function to handle user inputs and provide responses
def chatbot_response(user_input):
    # Convert the user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define some predefined rules and responses
    greetings = ["hello", "hi", "hey", "howdy"]
    goodbye = ["bye", "goodbye", "see you"]
    questions = ["what", "how", "why", "when", "where", "who"]
    compliments = ["great job", "well done", "awesome"]
    insults = ["stupid", "idiot", "dumb"]
    jokes = ["Tell me a joke.", "Give me a funny joke.", "Joke time!"]

    # Pattern matching for specific questions
    if re.search(r'\bweather\b', user_input):
        return "I'm sorry, I don't have access to real-time weather information."

    if re.search(r'\bjoke\b', user_input):
        return random.choice(["Why don't scientists trust atoms? Because they make up everything!", "What's orange and sounds like a parrot? A carrot!"])

    # Check if the user input matches any predefined rules
    if any(greeting in user_input for greeting in greetings):
        return "Hello! How can I assist you today?"

    elif any(word in user_input for word in goodbye):
        return "Goodbye! Have a great day!"

    elif any(word in user_input for word in questions):
        return "That's an interesting question, but I'm not equipped to answer it."

    elif any(word in user_input for word in compliments):
        return "Thank you! You're too kind."

    elif any(word in user_input for word in insults):
        return "I'm here to help. Please be polite."

    else:
        return "I'm sorry, I don't understand that."

# Main loop to take user inputs and provide responses
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)
