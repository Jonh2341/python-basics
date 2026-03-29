vegetables = {"carrot", "potato", "apple", "tomato"}

print(vegetables)

vegetables.add("cucumber")
print(vegetables)
vegetables.remove("apple")
print(vegetables)
vegetables.update(["onion", "beet"])
print(vegetables)

    # set operations
first_data = {1, 2, 3}
second_data = {3, 4, 5}

print(first_data | second_data)
    # union --> {1, 2, 3, 4, 5}
print(first_data & second_data)
    # intersection --> {3}
print(first_data - second_data)
    # difference --> {1, 2}