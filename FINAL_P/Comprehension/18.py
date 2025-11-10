'''
Q8. Multiply with Default Zero

Problem:
Given two unequal lists of numbers, use zip_longest() and list comprehension to multiply corresponding elements.
If one list is shorter, assume missing values as 0.

Sample Data:

a = [2, 4, 6, 8]
b = [3, 5]


Expected Output:

[6, 20, 0, 0]
'''

from itertools import zip_longest as zl

a = [2, 4, 6, 8]
b = [3, 5]

print([i*j for i, j in zl(a, b, fillvalue=0)])

print([i*j for i, j in zip(a, b)])