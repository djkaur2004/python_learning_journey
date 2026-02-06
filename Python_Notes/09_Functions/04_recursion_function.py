# Iterative Method
'''An iterative method solves a problem by repeating a set of instructions using loops'''
number = int(input("Enter a number to find its factorial: "))  # Enter a number to find its factorial: 5
factorial = 1
if number == 0:
  print("The factorial of 0 is 1")
else:
  for i in range(1, number+1):
    factorial = factorial * i
  print("The factorial of ",number,"using Iterative Methods is: ",factorial)  # The factorial of 5 using Iterative Method is: 120

# Recursive Method
'''A recursive method solves a problem by calling itself on a smaller input until it reaches a base case (the stopping condition).'''
def factorial_value(num):
  factorial = 1
  if num == 0:
    return factorial
  else:
    for i in range(1,num+1):
      factorial = factorial*i
    return factorial
  print("Factorial of 4 using Recursive Method: ",factorial_value(4))  # 24
