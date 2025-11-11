'''
Q9. Email Validation

Problem:
Create a custom exception InvalidEmailError.
Write a function to validate email format — it must contain @ and end with .com.
Raise the exception if the format is invalid.

Sample Input:

email = "hello.world"


Expected Output:

InvalidEmailError: Email must contain '@' and end with '.com'.
'''

class InvalidEmailError(Exception):
  def __init__(self, error):
    self.error = error

def ValidateMail(email):
  try:
    if '@' not in email:
      raise InvalidEmailError('E-Mail Must Contain @')
    elif not email.endswith('.com'):
      raise InvalidEmailError('E-Mail Must End With .com')
    else:
      print('E-Mail Is Valid!')
  except InvalidEmailError as Error:
    print(f'InvalidEmailError: {Error}')

ValidateMail('hello.world')