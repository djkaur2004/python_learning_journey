l1 = [1, 8, 7, 2, 21, 15]
print("\ngiven list ",l1)  # [1,8,7,2,21,15]

# SORTING OF A LIST
# sort() method is used to sort the given list in ascending order
l1.sort()
print("\nsorted list ",l1)  # [1,2,7,8,15,21]

# REVERSING A LIST 
# reverse() method is used to reverse a list
l1.reverse()
print("\nreverse of list is ",l1)  # [21,15,8,7,2,1]

# APPENDING A LIST OR ADDING AN ELEMENT TO THE GIVEN LIST 
l1.append(34) # adds 34 at the end of the list
print("\nafter appending the given list is ",l1)
# list append means adding an element to the end of the list 
# we can add as many elements in the list 
l1.append(76)
l1.append(98)
print("\nadding three elements in the given list we have ",l1)  # [21, 15, 8, 7, 2, 1, 34, 76, 98]

# INSERTING AN ELEMENT IN THE LIST 
l1.insert(2,100) # 100 is added at index 2 
print("\nlist after inserting an element in the list ",l1)  # [21, 15, 100, 8, 7, 2, 1, 34, 76, 98]
# here 2 is the index number and 100 is the element to be added

# REMOVING AN ELEMENT FROM THE LIST
l2 = [23, 45, 6, 77, 23, 90]
l2.remove(23)
print("\nafter removing an element from the list the new list formed is ",l2)  # [45, 6, 77, 23, 90]
# it removes the particular element from the list 
# if the element to be removed is present two times in the list, then it will remove the element whose index comes first. 

# POPING OR DELETING AN ELEMENT FROM THE LIST 
l3 = [34, 56 ,7 , 8, 9, 90]
l3.pop(4)
print("\npoping of list ",l3)  #  [34, 56, 7, 8, 90]
l3.pop(2)
print("\nagain doing poping of the list ",l3)  # [34, 56, 8, 90]
'''in poping it deletes the element present at a particular index
eg :- l3.pop(4)
it has deleted the element present on fourth index'''

# EXTEND METHOD
''' Using append method we can only add one element in the list. To add mulitple elements in the list we use
extend method, where the elements are added to the end of the list.'''
l4 = [1, 2, 3, "pyhton", 3.14, "200"]
l4.extend([40,50,60])
print("\nList after using extend method is : ",l4)  # [1, 2, 3, 'pyhton', 3.14, '200', 40, 50, 60]

# COUNT METHOD
# count() method is used to count the number of occurences of an element in the list
l4 = [1, 2, 3, 3.14, 40, 50, 2]
print("\nOccurence of 2 in the list : ",l4.count(2))  # 2



