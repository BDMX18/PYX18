'''
Q8. Find the GCD of a List

Problem:
Write a Python function that uses reduce to compute the GCD (Greatest Common Divisor) of a list of integers.

Sample Input:

nums = [48, 60, 72]


Expected Output:

12
'''

from functools import reduce

nums = [48, 60, 72]

def calcGCD(a, b):
  while a != b:
    if a > b:
      a -= b
    else:
      b -= a
  return a

result = reduce(calcGCD, nums)

print(result)