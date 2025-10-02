'''
Q4. Concatenate Strings

Problem:
Given a list of strings, use reduce to concatenate them into a single string separated by a space.

Sample Input:

words = ["reduce", "is", "powerful", "in", "Python"]


Expected Output:

"reduce is powerful in Python"
'''

from functools import reduce

words = ["reduce", "is", "powerful", "in", "Python"]

def concatenate(a, b):
  return a + ' ' + b

result = reduce(concatenate, words)

print(result)

print(reduce(lambda a,b: a + ' ' + b, words))