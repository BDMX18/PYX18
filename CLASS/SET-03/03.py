'''
Find the difference between the largest and smallest elements in a list

Problem:
Given a list of integers, find (max - min).

Example:

Input → [3, 7, 2, 9, 5]

Output → 7
'''

ip_list = [3,7,2,9,5]
max = min = ip_list[0]
for element in ip_list:
  if element > max:
    max = element
  elif element < min:
    min = element
print(max-min)