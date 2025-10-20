'''
Find the largest sum of two elements in a list

Problem:
Find the sum of the two largest numbers in a list.

Example:

Input → [5, 1, 8, 7, 3]

Output → 15 (8 + 7)
'''

ip_list = [5, 1, 8, 7, 3]
first = second = float('-inf')
for element in ip_list:
  if element > first:
    second = first
    first = element
  elif element > second and element != first:
    second = element
print(first + second)