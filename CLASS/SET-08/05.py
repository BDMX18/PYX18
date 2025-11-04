'''
Q5. Filter Students Who Passed

Write a Python program using list comprehension to filter students who scored more than 40 marks.

Sample Data:

students = {"Bibhu": 85, "Ravi": 39, "Lina": 56, "Kiran": 20}


Expected Output:

['Bibhu', 'Lina']
'''

students = {"Bibhu": 85, "Ravi": 39, "Lina": 56, "Kiran": 20}

filter_students = list(filter(lambda x: students[x] > 40, students))

print(filter_students)