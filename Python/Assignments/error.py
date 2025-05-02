def task_one():
    try:
        numbie = int(input("give me a number: \n"))
        print(f"100 divided by {numbie} is {100 / numbie}")
    except ValueError:
        print("Please input a valid number")
    except ZeroDivisionError:
        print("You cannot divide by zero!!")

def task_two():
    try:
        list = [1, 2]
        list[555]
    except IndexError:
        print("We are accesing a list at a position that does not exist")
    
    try:
        dicty = {"cat": "Tom", "mouse": "Jerry"}
        dicty["Tony Stark"]
    except KeyError:
        print("We are accessing a dictionary at a nonexistent Key")
    
    try:
        "waka waka" + 417
    except TypeError:
        print("You cannot add a string and integer")


def task3():
    try:
        num1 = int(input("Give me number 1: \n"))
        num2 = int(input("Give me number 2: \n"))
        val = num1 / num2
    except ValueError or ZeroDivisionError:
        print("Please input valid numbers")
    else:
        print(f"The result is {val}")
    finally:
        print("This block always exectues")
