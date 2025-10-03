'''
23. Recursive Sum with Default Argument

Problem: Implement recursive_sum(lst, i=0) that sums list recursively.
Input: recursive_sum([1,2,3,4])
Output: 10
'''

def recursive_sum(list, i=0):
  if i == len(list):
    return 0
  return list[i] + recursive_sum(list, i+1)

print(recursive_sum([1,2,3,4]))