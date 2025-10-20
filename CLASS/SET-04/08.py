'''
Find the second smallest element in a list

Problem:
Find the second smallest number in a list without using sort().

Example:

Input → [4, 1, 7, 2, 8]

Output → 2
'''

ip_list = [4,1,7,2,8]
first = second = float('inf')
for element in ip_list:
  if element < first:
    second = first
    first = element
  if element < second and element != first:
    second = element
print(second)