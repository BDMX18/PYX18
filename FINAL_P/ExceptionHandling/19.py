'''
Q2. Division Operation with Multiple Exceptions

Write a function safe_division(a, b) that performs division.
Handle:

ZeroDivisionError (when b = 0)

TypeError (when inputs are not numbers)

ValueError (if inputs are invalid strings like "abc")

Sample Data:

pairs = [(10, 2), (10, 0), (10, 'x'), ('a', 5)]
'''

pairs = [(10, 2), (10, 0), (10, 'x'), ('a', 5)]

def safe_division(a, b):
  try:
    result = a//b
  except ZeroDivisionError as error:
    print(error)
  except TypeError as error:
    print(error)
  else:
    print(result)

for a,b in pairs:
  safe_division(a, b)

