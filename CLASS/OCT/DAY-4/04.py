'''
Flatten a Nested List

Problem:
Write a function that takes a list of lists and flattens it into a single list.

Example:
Input: [[1, 2, [3]], [4, 5]]
Output: [1, 2, 3, 4, 5]
'''

# Flattening a list without recursion:
'''
Approach:
-> Here, at first we'll create a dummy of the given list, then we'll pop the first elemennt from the dummy list,
-> We'll check that element is an instance of list class, if it's then we'll add it dummy list, with a list being added to another list, it'll automatically get flattened.
-> If the element is not a list then in that case, we'll be directly adding it to the output list
'''

def flatten_list(ip_list):

  dummy = ip_list
  flatten = []

  while dummy:
    element = dummy.pop(0)
    if(isinstance(element, list)):
      dummy = element  + dummy
    else:
      flatten.append(element)
  
  return flatten

print(flatten_list([[1, 2, [3, [4,5,6]]], [4, 5]]))

# With recursion:

def recursive_flatten(ip_list):
  flatten = []
  for element in ip_list:
    if(isinstance(element, list)):
      flatten.extend(recursive_flatten(element))
    else:
      flatten.append(element)
  return flatten

print(recursive_flatten([[1, 2, [3, [4,5,6]]], [4, 5]]))

# Using List Comprehension:

ip_list = [[1, 2, 3], [4, 5]]
flat_list = (item for sub_list in ip_list for item in (sub_list if isinstance(sub_list, list) else [sub_list]))
print(list(flat_list))