'''
9. Flatten a List of Lists

Question: Use reduce() to flatten a list of lists into a single list.

Sample Data:
[[1, 2], [3, 4], [5, 6]]
Expected Output: [1, 2, 3, 4, 5, 6]
'''

from functools import reduce as r
print(r(lambda a, b: a+b, [[1, 2], [3, 4], [5, 6]]))