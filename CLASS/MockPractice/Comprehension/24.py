'''
Question 9:
From a nested dictionary of students and subjects, create a new dictionary with student names as keys and total marks as values.

students = {
    "Alice": {"Math": 85, "English": 78},
    "Bob": {"Math": 65, "English": 70},
    "Charlie": {"Math": 90, "English": 88}
}
'''

students = {
    "Alice": {"Math": 85, "English": 78},
    "Bob": {"Math": 65, "English": 70},
    "Charlie": {"Math": 90, "English": 88}
}

op_dict = {name: sum(marks.values()) for name, marks in students.items()}

print(op_dict)