'''
Q9. Product Calculator

Write a function multiply_all(*args) that multiplies all numbers passed as arguments.
If no argument is passed, print a message saying “No numbers provided.”

Sample Data:

multiply_all(2, 3, 4)
multiply_all()
'''

def multiply_all(*args):
  product = 1
  if args != ():
    for arg in args:
      product *= arg
    print('Product:', product)
  else:
    print('No Numbers Provided!')

multiply_all(2,3,4)
multiply_all()