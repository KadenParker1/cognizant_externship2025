
def factorial(n):
    if n == 0:
        return 1 
    return n * factorial(n - 1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

while True:
    val = input("Welcome to the Recursive Artistry Program! Choose an option: 1. Calculate Factorial 2. Find Fibonacci 4. Exit: \n")
    if not val.isdigit():
        print("Input must be an int. Try again.")
    else:
        if val == "3":
            print("Exiting")
            break
        elif val == "1":
            val2 = input("Please give me the number you want the factorial of: \n")
            print(f"The factorial of {val} is: {factorial(int(val2))} \n")
        elif val == "2":
            val3 = input("Please give me the number you want the Fibinacci of: \n")
            print(f"The {val}th Fibinacci number is: {fib(int(val3))}. \n")
