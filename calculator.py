def calculator(num1,num2,func):
    if (func == "addition"):
        print(num1 + num2)
    elif (func == "subtraction"):
        print(num1 - num2)
    elif (func == "multiply"):
        print(num1 * num2)
    elif (func == "division"):
        print(num1 / num2)
    elif (func == "power"):
        print(num1 ** num2)
    else:
        print("error")
    
calculator(13,7,"addition")
calculator(100,40,"subtraction")
calculator(22,2,"multiply")
calculator(69,3,"division")
calculator(4,2,"power")
