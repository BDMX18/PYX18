'''
6. Partition a List

Problem:
Given a list and a value x, rearrange the list so that all elements less than x come before all elements greater than or equal to x.

Example:
Input: [1, 4, 3, 2, 5, 2], x = 3
Output: [1, 2, 2, 4, 3, 5]
'''

def partition_list(ip_list, x):
  less = [element for element in ip_list if element < x]
  more_equal = [element for element in ip_list if element >= x]
  return less + more_equal

print(partition_list([1, 4, 3, 2, 5, 2], 3))