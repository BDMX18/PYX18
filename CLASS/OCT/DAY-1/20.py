'''
Find Common Elements in Two Lists

Given two lists of integers, find and print all the common elements between them using nested loops.
'''

list1 = [3, 5, 7, 9, 11, 13]
list2 = [2, 3, 5, 8, 13, 21]

common_list = []

for i in list1:
  for j in list2:
    if i == j and i not in common_list:
      common_list.append(i)
print(common_list)
