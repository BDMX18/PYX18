'''
From a list of employee dictionaries, use filter() to keep only employees with a salary greater than 50,000.
'''

employees = [
    {'name': 'Amit', 'salary': 45000},
    {'name': 'Riya', 'salary': 52000},
    {'name': 'Karan', 'salary': 61000},
    {'name': 'Neha', 'salary': 39000}
]

op_list = list(filter(lambda item: item['salary'] > 50000, employees))
print(op_list)