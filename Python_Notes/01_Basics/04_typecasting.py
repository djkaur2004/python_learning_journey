# Typecasting converts one data type into another.
# Example string to integer, integer to float, etc.

a = "355"
print(type(a))  # string
# print(a + 5) -> this will give an error as 'a' is a string and 5 is an integer 

# Converting 'a' string to integer
b = int(a)
print(type(b))  # integer

# Example 1
c = "10"
d = "5"
print(a + b)   # 105 (string concatenation)

c1 = int(c)
d1 = int(d)
print(c1 + d1)   # 15

# Another example: converting integer to float
x = 10
print(x)  # 10
print(type(x))  # integer

y = float(x)
print(y)  # 10.0
print(type(y))  # float
