'''
Find Dictionary with Maximum Value

Problem:
Given a list of dictionaries representing students and their marks, use reduce to find the dictionary of the student who scored the highest.

Sample Input:

students = [
    {"name": "Alice", "marks": 88},
    {"name": "Bob", "marks": 95},
    {"name": "Charlie", "marks": 91}
]


Expected Output:

{"name": "Bob", "marks": 95}
'''

students = [
    {"name": "Alice", "marks": 88},
    {"name": "Bob", "marks": 95},
    {"name": "Charlie", "marks": 91}
]

from functools import reduce

result = reduce(lambda a, b: a if a['marks'] > b['marks'] else b, students)

print(result)