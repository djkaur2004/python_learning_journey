myDict = {
    "Name": "John",
    "Age": 20,
    "Branch": "CSE"
}

# DICTIONARY METHODS
# 1. KEYS()
print(myDict.keys())
# prints the keys of the dictionary

# 2. VALUES()
print(myDict.values())
# prints the value of the dictionary

# 3. ITEMS()
print(myDict.items())
# prints the (key,value) for all the contents of the dictionary. 

# 4. UPDATE()
print(myDict)
updatedict = {
    "Marks" : 85,
    "Age" : "21",
    "Course" : "BTech"
}
myDict.update(updatedict)
print(myDict)  
# it updates the dictionary or we can say add new items to the dictionary

# 5. GET()
print(myDict.get("Name"))  # John
print(myDict["Name"])      # John

# DIFFERENCE BETWEEN GET() AND [] SYNTAX AND WHY GET() IS USED OR WE CAN SAY IS PREFERED.
print(myDict.get("name2"))  # None
# print(myDict["name2"])  # Error
''' if we write name2 directly then it throws an error as name2 is not present in the dictionary but if we use get() then 
it returns None instead of returning an error.'''

# POP METHOD
# Pop() method removes the item with specified key and returns its value
print("\nValue of key element removed from dictionary is : ",myDict.pop("Branch"))  # CSE

# POPITEM() METHOD
# Removes and returns the last key-value pair as a tuple
print("\nPoping last key-pair of dictionary : ",myDict.popitem())  # ('Course', 'BTech')

# CLEAR() FUNCTION
''' clear() functions removes all the elements of the dictionary.
It is written as myDict.clear()
NOTE:- clear() method only deletes the items present in the dictionary but the empty dictionary is still 
present there. Eg:- {}'''

