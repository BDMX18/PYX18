'''
Remove Duplicates from List

Input:

nums = [1, 2, 2, 3, 4, 4, 5]


Output:

[1, 2, 3, 4, 5]
'''

nums = [1, 2, 2, 3, 4, 4, 5]

original = []

for num in nums:
  if num not in original:
    original.append(num)
print(original)