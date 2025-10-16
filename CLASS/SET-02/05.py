'''
Count even and odd numbers in a list

Problem:
Count how many even and odd numbers exist in a given list.

Example:

Input → [10, 21, 4, 45, 66, 93]

Output → Even: 3, Odd: 3
'''
ip_list = [10, 21, 4, 45, 66, 93]
even_count = 0
odd_count = 0
for num in ip_list:
  if num%2==0:
    even_count += 1
  else:
    odd_count += 1
print(f'Even: {even_count}, Odd: {odd_count}')