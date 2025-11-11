'''
Custom Exception Handling Questions
Q1. Validate Age for Driving License

Problem:
Create a custom exception class InvalidAgeError.
Write a program that asks the user for their age and raises the exception if the age is below 18.
If valid, print "Eligible for driving license."

Sample Input:

Enter age: 16


Expected Output:

InvalidAgeError: Age must be 18 or above.
'''

class InvalidAgeError(Exception):
  def __init__(self, error_msg):
    self.error_msg = error_msg

try:
  age = int(input('Enter Your Age: '))
  if age < 18:
    raise InvalidAgeError('InvalidAgeError: Age must be 18 or above!')
  else:
    print('You\'re Eligible To Vote!')
except InvalidAgeError as IAE:
  print(IAE)
except ValueError as VE:
  print(VE)