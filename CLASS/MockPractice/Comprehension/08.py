'''
Question 8:
Swap keys and values in a dictionary.

original = {1: 'a', 2: 'b', 3: 'c'}
'''


original = {1: 'a', 2: 'b', 3: 'c'}

op_dict = {v:k for k, v in original.items()}

print(op_dict)