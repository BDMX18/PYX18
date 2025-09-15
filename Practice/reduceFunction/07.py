'''
7. Find the Smallest Number

Question: Given a list of numbers, use reduce() to find the smallest one.

Sample Data:
[45, 22, 78, 10, 33]
Expected Output: 10
'''

from functools import reduce as r
print(r(lambda a,b: a if a<b else b, [45, 22, 78, 10, 33]))