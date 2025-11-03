'''
Count Even and Odd Numbers

Input:

nums = [2, 5, 7, 8, 10, 13]


Output:

Even: 3  
Odd: 3
'''

nums = [2, 5, 7, 8, 10, 13]

even_count = 0
odd_count = 0
for num in nums:
  if num%2 == 0:
    even_count += 1
  else:
    odd_count += 1

print('Even Count:', even_count, 'Odd Count:', odd_count)