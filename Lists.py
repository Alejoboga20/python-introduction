"""
Lists are used to store multiple items in a single variable.
"""
my_list = ["apple", "banana", "cherry"]
my_number_list = [1, 2, 3, 4, 5, 123, 33, 3, 123]

# Accessing Items
print(my_list[1])  # Output: banana
print(my_number_list[2])  # Output: 3

print(my_number_list[1:3])

for item in my_list:
    print(item)


# Add Items
my_list.append("orange")
print(my_list)

# Delete Items
my_list.remove("banana")
print(my_list)

# Delete last item
my_list.pop()
print(my_list)

# Sort Items
my_number_list.sort()
print(my_number_list)
