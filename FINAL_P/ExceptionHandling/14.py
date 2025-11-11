'''
Q6. Marks Validation for Students

Problem:
Create a custom exception class InvalidMarksError.
Write a function that checks if all student marks are between 0 and 100.
If any mark is outside this range, raise the exception.

Sample Data:

marks = [85, 92, 105, 76]


Expected Output:

InvalidMarksError: Marks must be between 0 and 100.
'''

marks = [85, 92, 105, 76]


class InvalidMarkError(Exception):
  def __init__(self, message):
    self.message = message

def ValidateMarks(marks_list):
  try:    
    index = 0
    while index < len(marks_list):
      if marks_list[index] < 0 or marks_list[index] > 100:
        raise InvalidMarkError('InvalidMarksError: Marks must be between 0 and 100')
      index += 1
    else:
      print('Marks Are Valid!')
  except InvalidMarkError as E:
    print(E)

ValidateMarks(marks)