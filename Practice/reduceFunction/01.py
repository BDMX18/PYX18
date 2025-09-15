'''
1. Sum of All Numbers

Question: Given a list of integers, use reduce() to calculate the total sum.

Sample Data:
[3, 5, 7, 9, 11]
Expected Output: 35
'''

from functools import reduce as r

print('Sum: ',r(lambda a, b : a+b, [3, 5, 7, 9, 11]))