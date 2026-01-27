# WHAT IS A TUPLE
''' A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses.
Tuples are immutable and can not be modified after creation.'''

# TUPLE IS CREATED BY USING () 
mytuple = (23, 4, 5)
print(type(mytuple))

# PRINTING OF A TUPLE 
print("\ngiven tuple : ",mytuple)

# TUPLE CANNOT BE UPDATED UNLIKE A LIST 
# y = (45, 6, 90, 5, 56, 34)
# y[3] = 22
# print(y)
# we cannot the change the value of an element in a tuple 
# the above code gives an error 

# PRINTING OF AN EMPTY TUPLE 
t1 = ()
print("\nprinting of an empty tuple : ",t1)

# TUPLE WITH SINGLE ELEMENT 
t2 = (1) # wrong way to declare a tuple
print(t2)
print(type(t2))  # this returns integer type instead of a tuple
t3 = (1,) # correct way to define a single element in a tuple
print("\ntuple with single element : ",t3)
print(type(t3))
'''to declare a tuple with single element we have to put a commma after declaring or writing the 
element eg:- (2,)'''
# WHEN A TUPLE PRINTS IT ALWAYS PRINTS WITH () 

# TUPLE SLICING
t4 = (4,87,12,"tuple",0)
# Tuple can also store elements of different data types
print("\nTuple Slicing : ",t4[2:])

