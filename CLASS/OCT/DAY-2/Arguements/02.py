'''
Dynamic Calculator

Problem:
Write a function calculator(operation, *args) that performs a mathematical operation on a variable number of arguments.

operation can be "add", "multiply", "subtract", or "divide".

Raise an exception for invalid operations.

Sample Input 1:

calculator("add", 2, 3, 5)


Expected Output 1:

10


Sample Input 2:

calculator("multiply", 2, 3, 4)


Expected Output 2:

24
'''
from functools import reduce

def calculator(operation, *args):
  if operation == 'add':
    return reduce(lambda a,b: a+b, args)
  elif operation == 'multiply':
    return reduce(lambda a,b: a*b, args)
  else:
    return 'Invalid Inputs!'

print(calculator('add', 2,3,4,5,6,7))
print(calculator('multiply', 2,3,4,5,6,7))
