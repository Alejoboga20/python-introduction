"""
Sets are similar to lists but they are unordered and do not allow duplicate values.
We don't have an index to access the elements of a set.
"""
# Sets
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
print(len(my_set))  # Output: 5

for item in my_set:
    print(item)

# Add element
my_set.add(6)

# Add multiple elements
my_set.update([7, 8, 9])

# Remove and element
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}

# Remove all the elements
my_set.clear()
