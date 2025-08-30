'''
Check if a number is a perfect square.
Write a program to check if a given number such as 16, is a perfect square.
Input: 16
Expected Output: 16 is a perfect square.
'''

num = int(input('Enter A Number: '))
init = 1
perfect_square = False

while init <= num//2:
  if(init*init == num):
    perfect_square = True
    break
  init += 1
if(perfect_square):
  print(f'{num} is a perfect square!')
else:
  print(f'{num} is not a perfect square!')


