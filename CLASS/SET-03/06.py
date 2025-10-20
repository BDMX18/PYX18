'''
Convert two lists into a dictionary (keys from first, values from second)

Problem:
Handle cases where lists are of unequal length — extra keys should get value None.

Example:

Input →
keys = ['name', 'age', 'city']
values = ['Bibhu', 23]

Output →
{'name': 'Bibhu', 'age': 23, 'city': None}
'''

from itertools import zip_longest

keys = ['name', 'age', 'city']
values = ['Bibhu', 23]

op_dict = zip_longest(keys, values, fillvalue=None)
print(dict(op_dict))