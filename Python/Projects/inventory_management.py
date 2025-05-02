
"""Takes arguments dictionary, tuple of shape (quantity, price)""" # made an inventory class
class Inventory:
    def __init__(self):
        self.inventory = {}
    
    def add_item(self, name, quantity_price):
        """ quantity price is a tuple with shape (quantity, price)"""
        quantity, price = quantity_price
        self.inventory[name] = (quantity, price)
    
    def remove_item(self, name):
        if name in self.inventory:
            del self.inventory[name]
        else:
            print("Please Try Again, Name is not in Inventory") # throw an error if someone tries to delete something not in dictionary
    
    def update(self, name, new_quantity_price):
        """ Pass in a new quantity/price and update an already exisitng key in my inventory"""
        quantity, price = new_quantity_price
        self.inventory[name] = (quantity, price)

    def display(self):
        for keys, values in self.inventory.items():
            quant, price = values # unpack tuple
            print(f"Item: {keys}, Quantity: {quant}, Price: {price}")

    def display_value(self):
        for keys, values in self.inventory.items():
            quant, price = values # unpack tuple
            print(f"Item: {keys}, Value: {quant * price}")


# testing my class. It works great. 
# listy = Inventory()
# listy.add_item("mango", (3, .8))
# listy.add_item("Cow", (2, 650))
# listy.remove_item("Cow")
# listy.add_item("hat", (599, 50))
# listy.display()
# listy.display_value()
            

    