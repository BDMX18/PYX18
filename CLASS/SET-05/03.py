'''
Check if a number is an Armstrong number

Problem:
A number is Armstrong if the sum of its digits each raised to the power of the number of digits equals the number itself.

Example:

Input → 153

Output → Armstrong Number
'''

num = int(input('Enter A Number: '))
len = 0
num_len = num
sum = 0
while num_len != 0:
  num_len //= 10
  len += 1
dummy = num
while(dummy != 0):
  rem = dummy%10
  sum += rem**len
  dummy //= 10
if sum == num:
  print('Armstrong Number')
else:
  print('Not An Armstrong Number')
