'''
Find the sum of digits of a number

Problem:
Find the sum of all digits in an integer.

Example:

Input → 12345

Output → 15
'''

num = int(input('Enter A Number: '))
sum = 0
while num != 0:
  rem = num % 10
  sum += rem
  num //= 10
print('Sum:', sum)