'''
Q1. Store and Retrieve Student Records

Problem:
Write a Python program to store student records (name, roll number, marks) in a JSON file and retrieve them later for display.

Sample Data:

students = [
    {"name": "Alice", "roll": 1, "marks": 89},
    {"name": "Bob", "roll": 2, "marks": 76},
    {"name": "Charlie", "roll": 3, "marks": 92}
]
'''

import json

students = [
    {"name": "Alice", "roll": 1, "marks": 89},
    {"name": "Bob", "roll": 2, "marks": 76},
    {"name": "Charlie", "roll": 3, "marks": 92}
]

with open('student.txt', 'w') as FO:
  json.dump(students, FO)

with open('student.txt', 'r') as FO:
  data = json.load(FO)
  print(data)

