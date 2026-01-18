def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you?"

    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great! Thanks for asking 😊"

    elif user_input in ["what is your name", "who are you"]:
        return "I am a simple Python chatbot created for CodeAlpha internship."

    elif user_input in ["help"]:
        return "You can say: hello, how are you, what is your name, bye"

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day 👋"

    else:
        return "Sorry, I didn't understand that. Type 'help' for options."


def start_chatbot():
    print("🤖 Chatbot Started!")
    print("🤖 Type 'help' to see available commands.")
    print("🤖 Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("🤖 Chatbot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


start_chatbot()
