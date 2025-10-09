'''
8. Find Missing Numbers in a Range

Problem:
Given a list of integers from 1 to n with some missing, find the missing numbers.

Example:
Input: [1, 2, 4, 6, 7, 10], n = 10
Output: [3, 5, 8, 9]
'''

def missing_numbers(ip_list, n):
  missing = []
  for num in range(1, n):
    if num not in ip_list:
      missing.append(num)
  return missing

print(missing_numbers([1, 2, 4, 6, 7, 10], 10))

def missing_comp(ip_list, n):
  missing = [element for element in range(1, 10) if element not in ip_list]
  return missing

print(missing_comp([1, 2, 4, 6, 7, 10], 10))