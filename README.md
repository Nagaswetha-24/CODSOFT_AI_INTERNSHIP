# Task 1 - Rule-Based Chatbot

## Project Overview

This project is a simple Rule-Based Chatbot developed using Python.

The chatbot interacts with the user through the terminal and responds to different inputs using predefined rules and keyword matching.

## Features

- Responds to greetings
- Tells its name
- Responds to "How are you?"
- Explains what it can do
- Provides a help menu
- Displays the current date
- Displays the current time
- Provides information about the chatbot
- Responds to thank-you messages
- Handles unknown inputs
- Allows the user to exit using `bye`, `exit`, or `quit`

## Technologies Used

- Python
- VS Code
- Python built-in libraries:
  - `datetime`
  - `random`

## How It Works

The chatbot takes input from the user and checks it against predefined rules.

Based on the matched input, the chatbot gives an appropriate response.

For example:

- If the user enters `hello`, the chatbot gives a greeting.
- If the user enters `date`, it displays the current date.
- If the user enters `time`, it displays the current time.
- If the user enters `bye`, the chatbot ends the conversation.

## How to Run

1. Make sure Python is installed.
2. Open the project in VS Code.
3. Open `chatbot.py`.
4. Run the Python file.
5. Enter messages in the terminal.
6. Type `bye` to exit.

## Sample Interaction

```text
🤖 Welcome to My Rule-Based Chatbot!

You: hello
Bot: Hello! 😊 How can I help you?

You: what is your name
Bot: I am a Rule-Based Chatbot created using Python.

You: what can you do
Bot: I can respond to greetings, answer simple questions, show the date and time, and provide basic information.

You: time
Bot: The current time is ...

You: bye
Bot: Goodbye! Have a great day! 👋
