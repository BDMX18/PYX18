'''
Find Second Largest Number

Input:

arr = [10, 25, 3, 45, 30, 45]


Output:

Second Largest: 30
'''

arr = [10, 25, 3, 45, 30, 45]

first = second = float('-inf')

for num in arr:
  if num > first:
    second = first
    first = num
  elif num > second and num != first:
    second = num
print('Second Largest: ', second)