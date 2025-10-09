'''
Remove Duplicates from a List

Problem:
Write a function to remove duplicates from a list while preserving the original order.

Example:
Input: [1, 2, 2, 3, 4, 3, 5]
Output: [1, 2, 3, 4, 5]
'''

def remove_duplicates(ip_list):
  original = []
  for element in ip_list:
    if element not in original:
      original.append(element)
  return original

print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))