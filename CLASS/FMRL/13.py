'''
Given a list of integers, use filter() to remove all numbers that are perfect squares.
'''

import math

nums = [1, 2, 3, 4, 5, 9, 10, 16, 18, 25]

op_list = list(filter(lambda num: math.isqrt(num)**2 != num, nums))

print(op_list)