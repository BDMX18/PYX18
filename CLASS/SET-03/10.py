'''
Find the intersection of multiple lists

Problem:
Given a list of lists, find the common elements among all sublists.

Example:

Input → [[1, 2, 3, 4], [2, 3, 5], [0, 2, 3, 8]]

Output → [2, 3]
'''

ip_list = [[1, 2, 3, 4], [2, 3, 5], [0, 2, 3, 8]]
intersection = []
temp_int = ip_list[0]
for ip in range(1, len(ip_list)):
  for element in ip_list[ip]:
    if element in temp_int and element not in intersection:
      intersection.append(element)
print(intersection)

intersection = []
flatten = []
for element in ip_list:
  flatten += element
for element in flatten:
  if flatten.count(element) > 1 and element not in intersection:
    intersection.append(element)
print(intersection)