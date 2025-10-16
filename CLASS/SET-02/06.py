'''
Find the common elements between two lists

Problem:
Given two lists, find the elements that are common to both.

Example:

Input → list1 = [1, 2, 3, 4, 5], list2 = [4, 5, 6, 7, 8]

Output → [4, 5]
'''

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []
for num in list1:
  if num in list2:
    common.append(num)
print(common)
