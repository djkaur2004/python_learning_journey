# input() function in Python is used to take input from the user (keyboard)
# input() always returns a string(str).

name = input("Enter your name: ")
print(name)
print(type(name))  # string

# Taking integer as an input
num1 = int(input("Enter First Number: "))    # First Number = 5
num2 = int(input("Enter Second Number: "))   # Second Number = 2
sum = num1 + sum2
print("Sum of numbers: ",sum)  # Sum = 7

# Taking float as an input
num3 = float(input("Enter First number: "))    # First Number = 5.2
num4 = float(input("Enter Second Number: "))   # Second Number = 6.4
print("Sum of numbers: ",num3 + num4)  # Sum = 11.6
