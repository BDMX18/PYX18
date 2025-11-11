'''
Q4. Password Strength Checker

Problem:
Create a custom exception WeakPasswordError.
Write a function that checks password strength — the password must:

Be at least 8 characters

Contain at least one uppercase, one lowercase, one digit, and one special character

If any condition fails, raise WeakPasswordError with a descriptive message.

Sample Input:

password = "hello123"


Expected Output:

WeakPasswordError: Password must contain at least one uppercase and one special character.
'''

class WeakPasswordError(Exception):
  def __init__(self, error):
    self.error = error

def ValidatePassword(password):
  try:
    if len(password) < 8:
      raise WeakPasswordError('WeakPasswordError: The length of password should be 8 characters long!')
    elif not any(ch.islower() for ch in password):
      raise WeakPasswordError('WeakPasswordError: The password should have atleast one lowercase character!')
    elif not any(ch.isupper() for ch in password):
      raise WeakPasswordError('WeakPasswordError: The password should have atleast one uppercase character!')
    elif any(ch.isalnum() for ch in password):
      raise WeakPasswordError('WeakPasswordError: The password should have atleast one special character!')
    else:
      print('The password is valid!')
  except WeakPasswordError as E:
    print(E)

ValidatePassword('Hello123')