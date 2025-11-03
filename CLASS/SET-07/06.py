'''
Find All Unique Elements in Both Lists

Input:

list1 = [1, 2, 3, 4]  
list2 = [3, 4, 5, 6]


Output:

Unique elements: [1, 2, 5, 6]
'''

# Approach 1: By using set,

list1 = [1, 2, 3, 4]  
list2 = [3, 4, 5, 6]

a = set(list1)
b = set(list2)
print(list(a.symmetric_difference(b)))

# Approach 2: By using for loop

unique = []

for element in list1:
  if element not in list2:
    unique.append(element)

for element in list2:
  if element not in list1:
    unique.append(element)

print(unique)

# Approach 3: Using comprehension:

unique_l = [x for x in list1 if x not in list2] + [y for y in list2 if y not in list1]

print(unique_l)