'''
Q2. Update Employee Salary in JSON File

Problem:
Given an existing JSON file employees.json containing employee data, write a program to increase each employee’s salary by 10% and save the updated data back to the file.

Sample Data (employees.json):

[
  {"name": "John", "salary": 50000},
  {"name": "Jane", "salary": 60000},
  {"name": "Smith", "salary": 55000}
]
'''

employee = [
  {"name": "John", "salary": 50000},
  {"name": "Jane", "salary": 60000},
  {"name": "Smith", "salary": 55000}
]

import json

with open('employee.txt', 'w') as FO:
  json.dump(employee, FO)

with open('employee.txt', 'r') as FO:
  data = json.load(FO)

with open('employee.txt', 'w') as FO:
  for profile in data:
    profile['salary'] += profile['salary']*.10
  json.dump(data, FO)

with open('employee.txt', 'r') as FO:
  data = json.load(FO)
  print(data)