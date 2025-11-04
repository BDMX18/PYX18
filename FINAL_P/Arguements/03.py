'''
Student Report Generator (Default Argument)

Create a function student_report(name, marks=50) that prints the student’s name and marks.
If marks are not provided, use the default value.

Sample Data:

student_report("Bibhu")
student_report("Ananya", 86)
'''

def student_report(name, marks=33):
  report = f'Name: {name}, Marks: {marks}'
  return report

print(student_report("Bibhu"))
print(student_report("Ananya", 86))