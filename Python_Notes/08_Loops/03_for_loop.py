# For Loop
# A for loop is used to iterate over a sequence like a list, tuple, string, or range.

# SYNTAX
'''
for variable in sequence:
    # code block
'''  

# RANGE FUNCTION 
# Example 1: range(stop)
for i in range(5):
    print(i)  # 0,1,2,3,4
'''
1. In Python, range is used to generate a sequence of numbers.
2. range means a series of numbers within a given limit.
3. range(n) prints values from start to (n-1)'''

# Example 2: range(start, stop)
for i in range(1,8):
    print(i)  # 1,2,3,4,5,6,7
# Here the numbers will print from 1 to 7

# Example 3: range(start, stop, step)
for i in range(1,8,2):
    print(i)  # 1,3,5,7
# here 2 means the loop will skip to every 2nd number from 1 to 7

# Example 4: using for loop to print elements present in a list
fruits  = ['Apples', 'Mangoes', 'Kiwi', 'Orange', 'Watermelon']
for item in fruits:
    print(item)
# we can use any name in place of item. eg: we can write "for fruit in fruits" it means the same

# Example 5: for loop with else statement
# else statement will execute only when all the statements in for loop are executed successfully
for i in range(5):
    print(i)
else:
    print("This is the end of the for loop.")
  
''' NOTE:- else statement will only print when the program ends that is all the statements in for loop is executed.
If for loop is breaked while execution then else statement will not execute. Eg:- '''

for i in range(6):
    print(i)  # 0,1,2,3,4
    if(i==4):
        break
else:
    print("Sorry there is no i")  # this else will not print as for loop is breaked



