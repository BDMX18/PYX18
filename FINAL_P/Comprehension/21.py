'''
Q10. Create Indexed Dictionary of Combined Pairs

Problem:
Given two unequal lists — keys and values — use enumerate(), zip_longest(), and dictionary comprehension to create a dictionary where:

The key is the index (from enumerate)

The value is a tuple (key, value_from_other_list), using "None" for missing values.

Sample Data:

keys = ['x', 'y', 'z']
values = [10]


Expected Output:

{0: ('x', 10), 1: ('y', 'None'), 2: ('z', 'None')}
'''
from itertools import zip_longest as zl

keys = ['x', 'y', 'z']
values = [10]

print({i:(key, value) for i, (key, value) in enumerate(zl(keys, values, fillvalue='None'))})