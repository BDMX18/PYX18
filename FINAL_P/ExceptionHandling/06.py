'''
Q1. InvalidAgeError

Problem Statement:
Create a custom exception class InvalidAgeError.
Write a program that asks for a user’s age and raises InvalidAgeError if the age is less than 18.
If the age is valid, print “Access granted”.

Sample Input:

Enter your age: 15


Expected Output:

Error: Age must be 18 or above.
'''

class AgeValidator(BaseException):
  def __init__(self, msg):
    self.msg = msg

age = int(input('Enter Your Age: '))
if age > 18:
  print('You\'re Eligible To Vote!')
else:
  try:
    raise AgeValidator('You\'re Not Elgible To Vote!')
  except AgeValidator as AV:
    print(AV)