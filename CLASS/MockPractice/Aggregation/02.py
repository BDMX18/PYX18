'''
Question 2: Department and Employee

Scenario:
An Employee belongs to a Department. The department object is created independently, and multiple employees may refer to it.

Guideline:
👉 Create the Department object in main space, then pass it to multiple employees.

Question:
Implement classes Department and Employee.

The Department class should have attributes like dept_name, location.

The Employee class should have name, id, and a reference to the Department.

Create two employees working in the same department and print their info.
'''

class Employee:
  
  def __init__(self, name, id, dept):
    self.name = name
    self.id = id
    self.dept = dept
  
  def display(self):
    print(f'\nEmployee Name: {self.name} \nEmployee ID: {self.id} \nDepartment Name: {self.dept.dname} \nDepartment Location: {self.dept.dloc}')

class Department:
  
  def __init__(self, dname, dloc):
    self.dname = dname
    self.dloc = dloc

D1 = Department('Finance', 'London')

E1 = Employee('Ram', 110, D1)

E2 = Employee('Hari', 111, D1)

E1.display()
E2.display()