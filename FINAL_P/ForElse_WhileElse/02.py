'''
Q2. Search Element in List

Problem:
Check whether a specific number exists in a list using a for-else loop.

Sample Data:

numbers = [2, 4, 6, 8, 10, 12]
target = 5

Expected Output:
5 not found in the list.
OR (if target = 8):
8 found in the list.
'''

numbers = [2, 4, 6, 8, 10, 12]

num = int(input('Enter The Number You Want To Search: '))
# for number in numbers:
#   if num == number:
#     print(f'{num} found in the list')
#     break
# else:
#   print(f'{num} not found in the list')


index = 0
while index < len(numbers):
  if numbers[index] == num:
    print(f'{num} found in the list')
    break
  index += 1
else:
  print(f'{num} not found in the list')
  