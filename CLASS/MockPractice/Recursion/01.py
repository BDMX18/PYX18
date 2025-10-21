'''
Factorial of a Number
Write a recursive function to find the factorial of a given number.
'''

def recursive_factorial(n):
  if n == 0:
    return 1
  return n * recursive_factorial(n-1)

print(recursive_factorial(5))