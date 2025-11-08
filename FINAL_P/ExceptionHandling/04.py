'''
Handle Multiple Exceptions

Problem Statement:
Write a Python program that divides two numbers and handles both ValueError and ZeroDivisionError.
Ensure that a custom error message is printed for each case.

Sample Input:

Enter numerator: a  
Enter denominator: 5


Expected Output:

Error: Invalid input. Please enter numbers only.
'''

try:
  numerator = int(input('Enter The Numerator Value: '))
  dinominator = int(input('Enter The Dinominator Value: '))
  result = numerator/dinominator
  print(result)
except ValueError as VE:
  print('Data should be int type.')
except ZeroDivisionError as ZDE:
  print('Invalid Input, Please Enter Number Only!')