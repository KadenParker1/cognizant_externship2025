
while True:
    try: 
        option = int(input("Welcome to the Error-Free Calculator! Choose an operation: 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Exit: \n"))
    except ValueError:
        print("Needs to be valid inputs")
        continue
    if option == 1:
        try:
            num1 = int(input("Give number 1: \n"))
            num2 = int(input("Give number 2: \n"))
            print(f"Addition is: {num1 + num2}")
        except ValueError:
            print("Needs to be valid inputs")
            continue

    elif option == 2:
        try: 
            num1 = int(input("Give number 1: \n"))
            num2 = int(input("Give number 2: \n"))
            print(f"Subtractoin is: {num1 - num2}")
        except ValueError:
            print("Needs to be valid inputs")
            continue
    elif option == 3:
        try: 
            num1 = int(input("Give number 1: \n"))
            num2 = int(input("Give number 2: \n"))
            print(f"Multiplication is: {num1 * num2}")
        except ValueError:
            print("Needs to be valid inputs")
            continue
    elif option == 4:
        try: 
            num1 = int(input("Give number 1: \n"))
            num2 = int(input("Give number 2: \n"))
            print(f"Division is: {num1 / num2}")
        except ValueError:
            print("Needs to be valid inputs")
            continue
        except ZeroDivisionError:
            print("Cannot be Zero")
    elif option == 5:
        print("bye bye")
        break

