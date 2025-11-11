'''
Q5. Negative Number Error

Problem:
Create a custom exception NegativeNumberError.
Write a program that takes a list of numbers as input and raises the exception if any number is negative.

Sample Data:

numbers = [10, -4, 6, 8]


Expected Output:

NegativeNumberError: Negative numbers are not allowed.
'''

class NegativeNumberError(Exception):
  def __init__(self, error):
    self.error = error

def ValidateList(ip_list):
  try:
    for element in ip_list:
      if element < 0:
        raise NegativeNumberError('NegativeNumberError: Negative numbers are not allowed!')
    else:
      print('Input List is Valid!')
  except NegativeNumberError as E:
    print(E)

ValidateList([10, 6, 8])