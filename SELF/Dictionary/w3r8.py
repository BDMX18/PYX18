'''
Merge Two Python Dictionaries: Write a Python script to merge two Python dictionaries.
'''

# Approach 1: Iterate through the elements of dictionaries and update them in the new dictionary:
dict1 = {'A': 1, 'B':2}
dict2 = {'C': 3, 'D': 4}
dict3 = {}
for elements in dict1, dict2:
  dict3.update(elements)
print(dict3)

# Approach 2: 
dict1 = {'A': 1, 'B': 2}
dict2 = {}
dict2.update(dict1)
print(dict2)