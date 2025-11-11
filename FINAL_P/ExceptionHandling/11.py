'''
Q3. Username Validation

Problem:
Create a custom exception InvalidUsernameError.
Write a function that validates a username:

Must be at least 5 characters long

Must not contain spaces
If invalid, raise the custom exception with an appropriate message.

Sample Input:

username = "Jo e"


Expected Output:

InvalidUsernameError: Username must not contain spaces.
'''

class InvalidUsernameError(Exception):
  def __init__(self, error_msg):
    self.error_msg = error_msg

try:
  name = input('Enter Your Name:')
  if len(name) < 5:
    raise InvalidUsernameError('InvalidUsernameError: Username must be atleast 5 characters long!')
  elif ' ' in name:
    raise InvalidUsernameError('InvalidUsernameError: Username must not contain space!')
  else:
    print('Username is Valid!')
except InvalidUsernameError as E:
  print(E)