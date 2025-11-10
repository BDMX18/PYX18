'''
Q4. Combine Two Lists into a Dictionary

Problem:
Given two lists — one of students and one of marks — use dictionary comprehension with zip() to map each student to their mark.

Sample Data:

students = ['John', 'Emma', 'Raj', 'Olivia']
marks = [85, 92, 78, 90]


Expected Output:

{'John': 85, 'Emma': 92, 'Raj': 78, 'Olivia': 90}
'''

students = ['John', 'Emma', 'Raj', 'Olivia']
marks = [85, 92, 78, 90]

op_dict = {student:mark for student, mark in zip(students, marks)}

print(op_dict)