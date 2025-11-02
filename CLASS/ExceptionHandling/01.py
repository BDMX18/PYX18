'''
Handle Division by Zero
Write a program to divide two numbers entered by the user. Handle the ZeroDivisionError if the denominator is 0.
'''

a = int(input('Enter A Divident: '))
b = int(input('Enter The Divisor: '))
try:
  result = a/b
except ZeroDivisionError as ZDE:
  print(str(ZDE).title())
else:
  print(result)
