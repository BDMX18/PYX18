'''
Given a list of dictionaries with a 'marks' key, use reduce() to find the total marks obtained by all students.
'''

students = [
    {'name': 'Bibhu', 'marks': 78},
    {'name': 'Riya', 'marks': 85},
    {'name': 'Karan', 'marks': 92},
    {'name': 'Neha', 'marks': 74}
]

from functools import reduce

total = reduce(lambda acc, item: acc + item['marks'], students, 0)

print(total)