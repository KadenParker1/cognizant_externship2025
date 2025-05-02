
def greet_user(name):
    print("Hello " + name + " I would like to greet you...")

def add_numbers(a, b):
    return a + b

def describe_pet(pet_name, animal_type):
    print(f"I have a pet named {pet_name}. They are a {animal_type}.")

def make_sandwhich(*arg):
    sand_string = "I am making a sandwhich with:"
    for arg_val in arg:
        sand_string += (" " + arg_val)
    print(sand_string)

# make_sandwhich("hat", "cheese", "man", "fart") # testing sandwhich function
    
def factorial(n):
    if n == 0:
        return 1 
    return n * factorial(n - 1)    

# print(factorial(5))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

# print(fib(15)) # checking my fibinacci function