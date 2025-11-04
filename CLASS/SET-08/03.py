'''
Merge and Sort Two Lists

Write a Python program to merge two lists and sort them in ascending order without using the built-in sort() function.

Sample Data:

list1 = [9, 4, 7]
list2 = [1, 6, 2]


Expected Output:

[1, 2, 4, 6, 7, 9]
'''

list1 = [9, 4, 7]
list2 = [1, 6, 2]

merge = list1 + list2

for i in range(len(merge)):
  for j in range(i+1, len(merge)):
    if merge[i] > merge[j]:
      merge[i], merge[j] = merge[j], merge[i]

print(merge)