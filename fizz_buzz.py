def fizz_buzz(num):
    if (num % 3 == 0):
        print("fizz")
    elif (num % 5 == 0):
        print("buzz")
    elif (num % 3 and num % 5):
        print("Fizz Buzz")
    else:
        print("not fizz or buzz") 

fizz_buzz(9)
fizz_buzz(10)
fizz_buzz(6)
fizz_buzz(7)
