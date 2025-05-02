print("Welcome to the Personal Finance Tracker")
dicty = {}
def add_expense(data):
    description = input("Enter expense description: ")
    if not description:
        print("You didnt input anything")
        return
    cat = input("Enter category: ")
    if not cat:
        print("You didnt input anything")
        return
    try:
        amount = int(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    if not amount:
        print("You didnt input anything")
        return
    if cat in data:
        data[cat].append((description, amount))
    else:
        data[cat] = [(description, amount)]

def view_expenses(data):
    for cat, list_of_items in data.items():
        print(f"\n Category: {cat}")
        for item in list_of_items:
            print(f"\n      - {item[0]}: {item[1]}")

def view_summary(data):
    print("\n Summary:")
    for cat, list_of_items in data.items():
        total_val = 0
        for item in list_of_items:
            total_val += item[1]
        print(f"\n{cat}: {total_val}")

        
while True: # menue loop of the program
    try:
        num = int(input("\nWhat would you like to do? \n 1. Add Expense\n 2. View All Expenses\n 3. View Summary\n 4. Exit\n Choose an option: "))
    except ValueError:
        print("Must be integer")
        continue

    if num == 1:
        add_expense(dicty)
        continue
    if num == 2:
        view_expenses(dicty)
        continue
    if num == 3:
        view_summary(dicty)
        continue
    if num == 4:
        print("Bye Bye")
        break


    