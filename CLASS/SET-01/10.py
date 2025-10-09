'''
Merge two lists element-wise into a dictionary

Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]

Output: {'a': 1, 'b': 2, 'c': 3}
'''

keys = ['a', 'b', 'c']
values = [1, 2, 3]

op_dict = dict(zip(keys, values))
print(op_dict)