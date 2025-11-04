'''
Employee Details (Using kwargs)

Write a function employee_details(**kwargs) that accepts any number of keyword arguments representing employee details and prints them in the format:

key: value


Sample Data:

employee_details(name="Bibhu", age=23, position="Developer")
employee_details(id=102, name="Ananya", department="HR")
'''

def employee_details(**kwargs):
  for key in kwargs:
    print(key, ':', kwargs[key])
  return '_'*20

print(employee_details(name="Bibhu", age=23, position="Developer"))
print(employee_details(id=102, name="Ananya", department="HR"))
