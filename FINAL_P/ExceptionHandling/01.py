'''
Q1. Division with Exception Handling

Problem Statement:
Write a Python program that takes two numbers as input and performs division.
Handle cases where the denominator is zero or when the user provides invalid (non-numeric) input.

Sample Input:

Enter numerator: 10  
Enter denominator: 0


Expected Output:

Error: Division by zero is not allowed.
'''

try:
  numerator = int(input('Enter The Value For Numerator: '))
  dinominator = int(input('Enter The Value For Dinominator: '))
  try:
    result = numerator/dinominator
    print(result)
  except ZeroDivisionError as ZDE:
    print(ZDE)
except ValueError as VE:
  print(VE)
