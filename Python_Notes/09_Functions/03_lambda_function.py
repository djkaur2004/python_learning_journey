# Lambda Function
# A lambda function is a small, anonymous function (a function without a name) written in one single line.

# Syntax
# lambda arguments : expression

# Example 1: Comparison between Normal Function and Lambda Function
# Normal Function
def func_without_lambda(x):
    return x*2
print(func_without_lambda(20))  # 40

# Lambda Function
equiv = lambda x:x*2
print(equiv(20))  # 40
# much smaller than normal function

# Example 2: Square of a Number
square = lambda x: x * x
print(square(5))  # 25

# Example 3: Lmabda with multiple arguments
equiv = lambda x,y:x*y*2
print(equiv(20,40))  # 1600
