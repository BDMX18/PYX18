'''
Product of All Elements

Problem:
Write a Python function to calculate the product of all numbers in a list using reduce.

Sample Input:

nums = [2, 3, 4, 5]


Expected Output:

120
'''
from functools import reduce

nums = [2, 3, 4, 5]

result = reduce(lambda a,b: a*b, nums)

print('Product:', result)