'''
Q9. Using else and finally

Write a program that:

Takes user input for two numbers.

Divides them.

Prints “Division successful” in else block.

Prints “Program ended” in finally block.

Test all possible error cases.
'''

try:
  numerator = int(input('Enter Numerator: '))
  denominator = int(input('Enter Denominator: '))
  result = numerator /denominator
except ZeroDivisionError as error:
  print(error)
except ValueError as error:
  print(error)
else:
  print('Division Successfully!')
  print(result)
finally:
  print('Program Ended!')