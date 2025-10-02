'''
Flatten a List of Lists

Problem:
Use reduce to flatten a list of lists into a single list.

Sample Input:

nested = [[1, 2], [3, 4, 5], [6, 7]]


Expected Output:

[1, 2, 3, 4, 5, 6, 7]
'''

from functools import reduce
nested = [[1, 2], [3, 4, 5], [6, 7]]

result = reduce(lambda acc, list: acc + list, nested, [])
print(result)