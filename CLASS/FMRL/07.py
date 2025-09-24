'''
8. reduce() Interview Question

Q: Using reduce(), write a program to find the maximum number in a list without using the built-in max() function.

numbers = [10, 25, 3, 56, 78, 2, 89, 23]
'''

numbers = [10, 25, 3, 56, 78, 2, 89, 23]

from functools import reduce

print(reduce(lambda a,b: a if a>b else b, numbers))