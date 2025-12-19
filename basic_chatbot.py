def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi" or user_input == "hey":
            print("Chatbot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "who are you":
            print("Chatbot: I am chatbot!")

        elif user_input == "thanks" or user_input == "thank you":
            print("Chatbot: You're welcome!")

        elif user_input == "bye" or user_input == "goodbye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
