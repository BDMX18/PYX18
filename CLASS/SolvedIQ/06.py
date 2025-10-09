'''
Write a python program to convert two lists into a dictionary:
'''

# Approach 01: 
list1 = ['Naina', 'Kimi', 'Sheena']
list2 = [852345, 763567, 691276]

list_dict = {}
for k in range(len(list1)):
  for v in range(k, k+1):
    list_dict[list1[k]] = list2[v]
print(list_dict)


# Approach 02: 
def list_to_dict(list1, list2):
  return dict(zip(list1, list2))

print(list_to_dict(['Naina', 'Kimi', 'Sheena'], [852345, 763567, 691276]))