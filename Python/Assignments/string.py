# Task 1
stringy = "Python is amazing!"
print(f"First word: {stringy[0:6]}")
print(f"Amazing part: {stringy[10:17]}")
print(f"Reversed string: {stringy[::-1]}")

# Task 2
stringy = " hello, python world!"
print(stringy.strip())
print(stringy.capitalize())
print(stringy.replace("world", "universe"))
print(stringy.upper())

# Task 3
word = input("Please User, I request a word from you: \n")
backwards = word[::-1]
if word == backwards:
    print("This is a palindrome!")
else:
    print("No way Jose. Not a palindrome.")