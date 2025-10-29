'''
Reverse an integer (without converting it to string)

Problem:
Reverse a number using arithmetic operations only.

Example:

Input → 1234

Output → 4321
'''

num = int(input('Enter A Number: '))
reverse = 0
while(num != 0):
  rem = num % 10
  reverse = reverse * 10 + rem
  num //= 10
print(reverse)
