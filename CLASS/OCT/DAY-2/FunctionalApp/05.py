'''
Even Number Squares using map and filter

Problem:
Write a Python program that returns the square of all even numbers in a list using only map and filter.

Sample Input:

nums = [1, 2, 3, 4, 5, 6]


Expected Output:

[4, 16, 36]
'''

nums = [1, 2, 3, 4, 5, 6]

result = list(map(lambda a: a*a, filter(lambda a: a%2==0, nums)))

print(result)