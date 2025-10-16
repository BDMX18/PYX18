'''
Use reduce() to concatenate a list of strings into a single string, separated by a hyphen (-).
'''

words = ['Learn', 'Code', 'Repeat']

from functools import reduce as r

concatenate = r(lambda a, b: a+b, words)

print(concatenate)