'''
Check if a number is a palindrome

Problem:
Check whether a given integer reads the same backward and forward.

Example:

Input → 121

Output → Palindrome
'''

num = int(input('Enter A Number: '))
reverse = 0
dummy = num
while dummy != 0:
  rem = dummy % 10
  reverse = reverse * 10 + rem
  dummy //= 10
if reverse == num:
  print('Palindrome')
else:
  print('Not Palindrome')