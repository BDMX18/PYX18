'''
Q4. InvalidEmailError

Problem Statement:
Create a custom exception InvalidEmailError that is raised when an entered email does not contain @ or . symbols.
Prompt the user for an email and handle the exception with an appropriate message.

Sample Input:

Enter email: testemail.com


Expected Output:

Error: Invalid email format. Missing '@' or '.'.
'''

class InvalidEmailError(Exception):
  def __init__(self, error_msg):
    self.error_msg = error_msg

email = input('Enter Your E-Mail ID: ')
if '@' in email and '.' in email:
  print('Your E-Mail Is Valid!')
else:
  try:
    raise InvalidEmailError('Error: Invalud E-Mail Format. Missing \'@\' or \'.\'')
  except InvalidEmailError as IEEE:
    print(IEEE)
