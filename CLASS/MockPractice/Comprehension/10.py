'''
Question 10:
Given two lists of equal length, create a dictionary mapping elements from the first list to elements in the second.

keys = ["name", "age", "city"]
values = ["Alice", 23, "New York"]
'''

keys = ["name", "age", "city"]
values = ["Alice", 23, "New York"]

op_dict = zip(keys, values)

print(dict(op_dict))

op_dict = {keys[k]: values[v] for k in range(len(keys)) for v in range(len(values)) if k == v}

print(op_dict)