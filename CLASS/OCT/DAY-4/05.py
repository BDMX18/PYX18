'''
Find Common Elements Between Two Lists

Problem:
Write a function to find the common elements between two lists without using set intersection.

Example:
Input: [1, 2, 3, 4] and [3, 4, 5, 6]
Output: [3, 4]
'''

def common_list(list_one, list_two):
  common = []
  for lo in list_one:
    for lt in list_two:
      if lo == lt:
        common.append(lo)
  return common

print(common_list([1, 2, 3, 4], [3, 4, 5, 6]))