'''
Q6. Email Validation

Create a custom exception InvalidEmailError.
Write a function to check if an email:

Contains @

Ends with .com
Raise an exception otherwise.

Sample Data:

emails = ["john@gmail.com", "user123", "admin@company.org"]
'''

emails = ["john@gmail.com", "user123", "admin@company.org"]

class InvalidEmailError(Exception):
  def __init__(self, msg):
    self.msg = msg

for email in emails:
  try:
    if '@' not in email:
      raise InvalidEmailError('Mail Should Have @')
    elif not email.endswith('.com'):
      raise InvalidEmailError('Mail Should End With .com')
    else:
      print('Mail Is Valid!')
  except InvalidEmailError as error:
    print(f'Error: {error}')
  else:
    print(email)