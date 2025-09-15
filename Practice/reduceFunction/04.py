'''
4. Maximum Number in a List

Question: Given a list of integers, use reduce() to find the maximum number.

Sample Data:
[23, 89, 15, 92, 37]
Expected Output: 92
'''

from functools import reduce as r
print(r(lambda a, b: a if a>b else b, [23, 89, 15, 92, 37]))