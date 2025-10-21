'''
Compare Two Student Objects
Define a Student class with marks and name. Overload the > operator to compare students based on marks.
'''

class Student:

  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def __gt__(self, other):
    return self.marks > other.marks

  
s1 = Student('Bibhu', 57)
s2 = Student('Dutta', 87)

if (s1 > s2):
  print(f'{s1.name} has more marks than {s2.name}')
else:
  print(f'{s2.name} has more marks than {s1.name}')
