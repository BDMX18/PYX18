'''
2. Product of All Numbers

Question: Given a list of integers, use reduce() to find the product of all numbers.

Sample Data:
[2, 4, 6]
Expected Output: 48
'''

from functools import reduce as r

print(r(lambda a,b : a*b, [2, 4, 6]))