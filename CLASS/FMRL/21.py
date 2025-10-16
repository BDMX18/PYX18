'''
Given a list of integers, use reduce() to find the maximum element without using the max() function.
'''

nums = [12, 45, 7, 89, 23, 56]

from functools import reduce

maximum = reduce(lambda a, b: a if a > b else b, nums)

print(maximum)