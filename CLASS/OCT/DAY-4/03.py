'''
3. Rotate a List

Problem:
Given a list and a number k, rotate the list to the right by k elements.

Example:
Input: [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
'''

def rotate_list(ip_list, k):
  op_list = ip_list[-k:] + ip_list[:-k]
  return op_list

print(rotate_list([1,2,3,4,5], 3))
  