'''
Question 8:
Given two lists, create a dictionary where keys are elements from the first list, values are squared elements from the second list, but include only if the squared value is even.

keys = [1, 2, 3, 4]
values = [1, 2, 3, 4]
'''

keys = [1, 2, 3, 4]
values = [1, 2, 3, 4]

op_dict = {k:v**2 for k, v in zip(keys, values) if (v**2)%2==0}

print(op_dict)