''' 
1. A set in python is an unordered collection of unique items. Sets are similar to list and dictionaries, but
they don't have duplicate values and don't support indexing or slicing.
2. Sets are unchangeble, meaning you cannot change items of the set once created.
'''

mySet = {1, 2, 3, 4, 1}
print(type(mySet))
print(mySet)
# In sets repeated values are not printed 
# It is a collection of non-repetitve values 

# EMPTY SET 
# IMPORTANT : THIS SYNTAX WILL CREATE AN EMPTY DICTONARY AND NOT AN EMPTY SET.
set1 = {}
print(type(set1))

# AN EMPTY SET CAN BE CREATED USING THE BELOW SYNTAX : 
set2 = set()
print(type(set2))

# VALUES IN A SET CANNOT BE CHANGED.

''' We can convert a list into set using set() constructor.'''
myList = [4,5,68,2,4]
print("\nConvert list to set : ",set(myList))

# Adding an item in the set
set3 = {1,4,68,34,5} 
set3.add(2)
print("\nAfter adding element in the set the updated set is : ",set3)

''' Sets can also contain different datatypes just like list.'''
set4 = {"Carla",19,False,5.6,19}
print("\n",set4)

