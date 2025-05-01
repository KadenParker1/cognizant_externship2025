age = int(input("How old are you? "))
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
if age < 18:
    print(f"Oops! You’re not eligible yet. But hey, only {18 - age} more years to go!") # use an f-string subtracting user input from 18 to get the years remaining value.
