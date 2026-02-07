# Formatting in Strings
'''String formatting in Python is a technique used to insert variables and values into a string in a readable and controlled manner.

Why do we need string formatting?
Because strings often need to change based on:
- User input
- Calculations
- Program results
Instead of hard-coding values, formatting lets Python fill them in automatically.
'''

# Common ways to do string formatting in Python

# format() method
template1 = "Hello, my name is {} and I am {} years old."
formatted_string1 = template1.format("Alice",30)
print(formatted_string1)  # Hello, my name is Alice and I am 30 years old.

# Formatting using Index
template2 = "Hello, my name is {0} and I am {1} years old. Did I mention my name is {0}?"
formatted_string2 = template2.format("Alice",30)
print(formatted_string2)  # Hello, my name is Alice and I am 30 years old. Did I mention my name is Alice?

# Keyword Formatting
''' In this method, you use named placeholders in the string and then pass the values as keyword arguments to the 
format() method.'''
template3 = "Hello, my name is {name} and I am {age} years old."
formatted_string3 = template3.format(name = "Bob",age = 45)
print(formatted_string3)  # Hello, my name is Bob and I am 45 years old.

# Formatting of Numbers
# Example 1
pi = 3.14159
print(f"Pi value: {pi:.2f}")  # here 2 numbers after decimal will be printed 
# Output-> Pi value: 3.14
# Example 2
print(f"Pi value: {pi:.3f}")  # here 3 numbers after decimal will be printed
# Output-> Pi value: 3.141

# Formatting using f-string (most recommended)
name = "Jasper"
age = 20
print(f"Hello, my name is {name} and I am {age} years old.")  # Hello, my name is Jasper and I am 20 years old.
