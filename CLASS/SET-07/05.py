'''
Check if Two Lists Have Common Elements

Input:

list1 = [1, 2, 3, 4]  
list2 = [3, 5, 6]


Output:

Common elements: [3]
'''

list1 = [1,2,3,4]
list2 = [3,5,6]

common = []

for element in list1:
  if element in list2:
    common.append(element)

print(common)

common_l = [x for x in list1 if x in list2]

print(common_l)