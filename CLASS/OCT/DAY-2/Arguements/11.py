'''
Multiply All with *args

Problem: Write multiply_all(*args) that multiplies all passed numbers.

Input: multiply_all(2, 3, 4)

Output: 24
'''

def multiplyAll(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(multiplyAll(2,3,4,5))