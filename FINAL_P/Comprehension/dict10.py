'''
Write a dictionary comprehension to remove all keys with None or empty values from a given dictionary.

data = {'name': 'Bibhu', 'age': None, 'city': '', 'country': 'India'}
# Expected Output: {'name': 'Bibhu', 'country': 'India'}
'''

data = {'name': 'Bibhu', 'age': None, 'city': '', 'country': 'India'}

op_dict = {key:value for key,value in data.items() if bool(value) == True}

print(op_dict)