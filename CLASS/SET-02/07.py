'''
Count occurrences of each element in a list

Problem:
Create a dictionary showing how many times each element appears.

Example:

Input → [1, 2, 2, 3, 3, 3]

Output → {1: 1, 2: 2, 3: 3}
'''

ip_list = [1, 2, 2, 3, 3, 3]

occurance = {}
count = 1
for num in ip_list:
  if num not in occurance:
    occurance[num] = count
  else:
    occurance[num] += 1
print(occurance)
