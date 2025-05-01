password = input("Please create a password: \n")

while True:
    if len(password) < 8:
        print("Password is too short, try again")
        password = input("Please create a password: \n")
        continue
    if not any(p.isupper() for p in password):
        print("Needs Uppercase")
        password = input("Please create a password: \n")
        continue
    if not any(p.islower() for p in password):
        print("Needs Lowercase")
        password = input("Please create a password: \n")
        continue
    if not any(p.isdigit() for p in password):
        print("Needs Digit")
        password = input("Please create a password: \n")
        continue
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    special_bool = False
    for sp in special_characters:
        if sp in password:
            special_bool = True
            break
    if not special_bool:
        print("Needs Special Character")
        password = input("Please create a password: \n")
        continue
    print("Your Password is strong!")
    break