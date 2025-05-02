# task 1
fruits = ["banana", "watermelon", "blueberry", "mango", "coconut"]
fruits.append("apple")
fruits.remove("banana")
print(fruits[::-1]) # add one new fruit, remove a fruit, and print the list in reverse

# task 2
personal_info = {"name": "Kaden", "age": 22, "city": "Provo"}
personal_info.update({"favorite color": "blue"})
personal_info["city"] = "Salt Lake City"

for keys, values in (personal_info).items():
    print(f"Key: {keys}")
    print(f"Values: {values}")

# task 3
favorite_things = ("Labyrinth", "Marching Bands of Manhattan", "The Bell Jar")
# favorite_things[2] = "East From Eden" # this results in the following error: TypeError: 'tuple' object does not support item assignment
print(len(favorite_things))