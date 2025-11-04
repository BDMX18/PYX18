'''
Level 2 – Intermediate

Given two lists, one of keys and one of values, combine them into a dictionary using dictionary comprehension.

keys = ['name', 'age', 'city']
values = ['Bibhu', 23, 'Odisha']
# Expected Output: {'name': 'Bibhu', 'age': 23, 'city': 'Odisha'}
'''

keys = ['name', 'age', 'city']
values = ['Bibhu', 23, 'Odisha']

info_dict = {keys[key]:values[value] for key in range(len(keys)) for value in range(len(values)) if key == value}

print(info_dict)

