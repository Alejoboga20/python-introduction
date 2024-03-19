"""
String Formatting
"""

first_name = "John"
print("Hello, %s!" % first_name)

last_name = "Doe"
username = first_name + " " + last_name

# The %s is a placeholder that is replaced by the value of the variable following the % symbol.
print("Hello, %s!" % username)

# string formatting
# f is a prefix that tells Python to replace the variable name with its value.
print(f"Hello, {username}!")

sentence = "Hello, {} {}!"
last_name_sentence = "User"
print(sentence.format(username, last_name_sentence))
print(f"Hello, {username}! Your last name is {last_name_sentence}.")