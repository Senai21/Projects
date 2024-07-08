def chat_bot():
    print("Welcome gang!")
    response = input("What can I help you with?\n")
    if (response == "calculate"):

        func = input("what do you wanna calculate\n")
        num1 = int(input("what's your first number?\n"))
        num2 = int(input("what's your second number?\n"))

        result = 0

        if (func == "addition"):
            result = num1 + num2
        elif (func == "subtraction"):
            result = num1 - num2
        elif (func == "multiply"):
            result = num1 * num2
        elif (func == "division"):
            result = num1 / num2
        elif (func == "power"):
            result = num1 ** num2
        
        print("Your result is ", result)

chat_bot()
