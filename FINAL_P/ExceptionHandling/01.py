'''
Custom Exception: Age Validation
Create a custom exception InvalidAgeError. Raise it if the user enters an age less than 18.
'''

class AgeValidation(Exception):
  def __init__(self, msg):
    self.msg = msg

try:
  age = int(input('Enter Your Age: '))
  if age < 18:
    raise AgeValidation('You\'re Age Is Under 18')
except AgeValidation as AV:
  print(AV)
else:
  print('Your\'re Eligiible For Voting!')