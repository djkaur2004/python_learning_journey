'''String in Python is a sequence of characters enclosed within single, double or triple quotes. Strings are a
fundamental data type in Python used to represent text.'''

greeting = "Good Morning, "
name = "Augustus"
print(greeting + name) # joining of two strings

c = greeting + name
print(c)  # Good Morning, Augustus

print("Hello, ",name)  # Hello,  Augustus

# STRING INDEXNG
a = "Beatrice"
print(a[5])  # i

# STRING SLICING
print(a[0:5])  # Beatr
# charaters 0,1,2,3,4 will print but 5th character will not print
# this is called slicing of strings or division of a string into smaller portion or selecting few characters

print(a[:5])  # it is same as name [0;5]
# blank space doesn't show error instead it automatically starts with 0 
# here before : 0 will come 

print(a[0:])  # same as [o:7] here output is: Beatrice
# it will print the whole line or string from the character which we have introduced eg:
print(a[4:])  # rice
# here after : last character will come which is 7 in this case
 
b = a[-5:-1]
print(b) # same as characters from [3:7] here output is: tric

d = a[0:7:2]
print(d)  # Barc
# here characters from [0:7] will be selected and 2 after : means between 0 to 7 every second character will 
# print. if we change 2 to 3 then it will skip to every third character

e = a[0:7:3]
print(e)  # Btc
# here string will print for every 3rd character
