from datetime import datetime

print("🤖           WELCOME TO AI CHATBOT           🤖")
print("Bot: Hello! I am your Rule-Based AI Chatbot.")
print("Bot: How can I help you today?")
print("Bot: Type 'help' to see what I can do.")
print("Bot: Type 'bye' to exit.\n")

while True:

    user = input("You: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Namaste! Nice to meet you.")

    elif user in ["help", "what can you do", "how can you help me"]:
        print("\nBot: I can help you with:")
        print("1. Greetings")
        print("2. Tell my name")
        print("3. Tell who made me")
        print("4. Explain AI")
        print("5. Tell the current time")
        print("6. Tell today's date")
        print("7. Tell a joke")
        print("8. Simple calculator")
        print("9. Respond to thanks")
        print("10. Exit the chatbot\n")
         
    

    elif user == "what is your name":
        print("Bot: My name is AI Chatbot.")


    elif user == "who made you":
        print("Bot: I was created by swati.")

    elif user == "how are you":
        print("Bot: I am doing great! Thank you for asking.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")
        print("Bot: It enables machines to think and solve problems.")

    elif user == "time":
        print("Bot: Current time is",
              datetime.now().strftime("%H:%M:%S"))

    elif user == "date":
        print("Bot: Today's date is",
              datetime.now().strftime("%d-%m-%Y"))

    elif user == "joke":
        print("Bot: Why did the computer go to the doctor?")
        print("Bot: Because it caught a virus!")

    elif user == "calculator":

        try:
            a = float(input("Enter first number: "))
            op = input("Enter operator (+,-,*,/): ")
            b = float(input("Enter second number: "))

            if op == "+":
                print("Bot: Result =", a + b)

            elif op == "-":
                print("Bot: Result =", a - b)

            elif op == "*":
                print("Bot: Result =", a * b)

            elif op == "/":
                if b == 0:
                    print("Bot: Cannot divide by zero.")
                else:
                    print("Bot: Result =", a / b)

            else:
                print("Bot: Invalid operator.")

        except:
            print("Bot: Invalid input.")

    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome!")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'help' to know what I can do.")