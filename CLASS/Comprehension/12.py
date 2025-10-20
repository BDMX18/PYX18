'''
Given two lists: keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary mapping keys to values.
'''

keys = ['a', 'b', 'c']
values = [1, 2, 3]

op_list = {keys[key]: values[value] for key in range(len(keys)) for value in range(len(values)) if key == value}

print(op_list)

op_dict = zip(keys, values)

print(dict(op_dict))