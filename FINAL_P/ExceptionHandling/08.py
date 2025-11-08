'''
Q3. InvalidGradeError

Problem Statement:
Define a custom exception InvalidGradeError that should be raised if a student’s grade is not between 0 and 100.
The program should accept multiple grades and store only valid ones.

Sample Input:

Grades = [95, 102, 85, -5, 76]


Expected Output:

Error: Invalid grade 102. Must be between 0 and 100.
Error: Invalid grade -5. Must be between 0 and 100.
Valid grades: [95, 85, 76]
'''

class InvalidGradeError(Exception):
  def __init__(self, error_msg):
    self.error_msg = error_msg

grades = [95, 102, 85, -5, 76]

valid_grades = []

for grade in grades:
  if grade >= 0 and grade <= 100:
    valid_grades.append(grade)
  else:
    try:
      raise InvalidGradeError(f'Error: Invalid Grade {grade}. Must be between 0 and 100')
    except InvalidGradeError as IGE:
      print(IGE)
print(valid_grades)


