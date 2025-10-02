'''
Find the Maximum Number in a List

Problem:
Write a Python program to find the maximum element from a list of integers using reduce.

Sample Input:

nums = [12, 45, 67, 23, 89, 34]


Expected Output:
89
'''

from functools import reduce as r

nums = [12, 45, 67, 23, 89, 34]

result = r(lambda a, b: a if a > b else b, nums)

print('Maximum Number:', result)

