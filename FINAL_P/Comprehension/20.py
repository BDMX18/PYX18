'''
Q9. Combine Unequal Data into Tuples

Problem:
Given two lists — names and ages — of different lengths, use zip_longest() and list comprehension to form tuples (name, age), using "Unknown" for missing ages.

Sample Data:

names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30]


Expected Output:

[('Alice', 25), ('Bob', 30), ('Charlie', 'Unknown'), ('David', 'Unknown')]
'''

from itertools import zip_longest as zl

names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30]


print([(name, age) for name, age in zl(names, ages, fillvalue='Unknown')])