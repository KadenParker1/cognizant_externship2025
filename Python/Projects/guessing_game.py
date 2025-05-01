import random
number_to_guess = random.randint(1, 100)

boolval = False
guesses = 0
while not boolval:
    guesses += 1
    guess = int(input("Guess the number: \n"))
    if guess == number_to_guess:
        print("Congratulations! You've guessed it!")
        print(f"Your total number of guesses was: {guesses}")
        boolval = True
    elif guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again")