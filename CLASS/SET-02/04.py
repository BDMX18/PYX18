'''
Find all unique elements from a list

Problem:
Given a list with duplicate elements, return a new list containing only unique elements (preserving order).

Example:

Input → [1, 2, 2, 3, 4, 4, 5]

Output → [1, 2, 3, 4, 5]
'''

ip_list = [1, 2, 2, 3, 4, 4, 5]
op_list = []
for num in ip_list:
  if num not in op_list:
    op_list.append(num)
print(op_list)