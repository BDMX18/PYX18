'''
Using reduce(), find the product of all numbers in a list.
'''

nums = [2, 3, 4, 5]

from functools import reduce as r

product = r(lambda a,b: a*b, nums)

print(product)