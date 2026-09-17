from datetime import datetime
import random

# Welcome message
print("🤖 Welcome to My Rule-Based Chatbot!")
print("Type 'help' to see what I can do.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()

    # Greetings
    if user in ["hi", "hello", "hey", "good morning", "good evening"]:
        responses = [
            "Hello! 😊 How can I help you?",
            "Hi there! 👋 Nice to meet you!",
            "Hey! 😊 What would you like to know?"
        ]
        print("Bot:", random.choice(responses))

    # Name
    elif "your name" in user or "who are you" in user:
        print("Bot: I am a Rule-Based Chatbot created using Python.")

    # How are you
    elif "how are you" in user or "how r u" in user:
        print("Bot: I'm doing great! 😄 Thanks for asking.")

    # What can the chatbot do
    elif "what can you do" in user:
        print("Bot: I can respond to greetings, answer simple questions, show the date and time, and provide basic information.")

    # Help
    elif user == "help":
        print("Bot: Here are the commands you can try:")
        print("- hi / hello")
        print("- what is your name")
        print("- how are you")
        print("- what can you do")
        print("- date")
        print("- time")
        print("- about")
        print("- bye")

    # Date
    elif user == "date":
        today = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", today)

    # Time
    elif user == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print("Bot: The current time is", current_time)

    # About the chatbot
    elif user == "about":
        print("Bot: I am a simple Python chatbot that uses predefined rules and keyword matching to respond to users.")

    # Thank you
    elif "thank" in user or "thanks" in user:
        print("Bot: You're welcome! 😊")

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day! 👋")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'help' to see the available commands.")
