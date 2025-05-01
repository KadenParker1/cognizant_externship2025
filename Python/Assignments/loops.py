# Task 1
numbie = int(input("Give me a starting number or else: \n"))
print(" \n \n \n" * 10) # use some new liens to clear terminal a bit
while numbie != 0:
    print(numbie)
    numbie -= 1
print("Number has terminated. Ha Ha Ha")

# Task 2

numbie2 = int(input("Give me a number or else: \n"))
print(" \n \n \n" * 10)
for i in range(1, 11):
    print(f"{numbie2} x {i} = {numbie2 * i}")


# Task 3
numbie3 = int(input("Give me a number or else: \n"))
val = 1
for i in range(1, numbie3 + 1):
    val = i * val
print(f"The factorial of {numbie3} is {val}.")