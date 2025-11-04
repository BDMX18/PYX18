'''
Level 3 – Advanced / Trick Questions

Write a dictionary comprehension to invert a dictionary — swap keys and values.

data = {'a': 1, 'b': 2, 'c': 3}
# Expected Output: {1: 'a', 2: 'b', 3: 'c'}
'''

data = {'a': 1, 'b': 2, 'c': 3}

inverted_dict = {value:key for key, value in data.items()}

print(inverted_dict)