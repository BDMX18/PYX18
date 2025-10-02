'''
Flatten a Nested List using reduce

Problem:
Write a Python function to flatten a nested list of integers using reduce.

Sample Input:

nested = [[1, 2], [3, 4, 5], [6]]


Expected Output:

[1, 2, 3, 4, 5, 6]
'''

nested = [[1, 2], [3, 4, 5], [6]]

from functools import reduce

result = reduce(lambda acc, sublist: acc + sublist, nested, [])

print(result)