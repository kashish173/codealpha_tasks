def chatbot():
    print("Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if user == "hello":
            print("Bot: Hi there!")
        elif user == "how are you":
            print("Bot: I'm good, thanks!")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand.")

chatbot()
