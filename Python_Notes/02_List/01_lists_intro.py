# List is an ordered collection of data with elements separated by a comma and enclosed within a square bracket.
# List are mutable and can be modified after creation.

# Creating a list
list1 = [1,2,3,4,5]
print(list1)  # [1,2,3,4,5]
print(type(list1))

# List can store different datatypes
list2 = [23, 8.9, "English", True]
# changing value of an element in the list (mutable)
list2[63] = 96
print(list2)  # [96, 8.9, "English", True]

# print elements using index
fruits = ["apple", "orange", "grapes", "pear", "banana"]
print(fruit[0])  # apple
print(fruit[1])  # orange
print(fruit[2])  # grapes

# List Slicing
# List slicing means taking a part (slice) of a list using index range.
list3 = ["sam", "rohan", "sachin", 98, 78.9, 88]
print("Slicing of list ",c[0:4])  # ["sam", "rohan", "sachin", 98]
