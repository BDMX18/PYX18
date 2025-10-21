'''
Overload Equality Operator (==)
Implement a class Person and overload the == operator to check equality based on both name and age.
'''

class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __eq__(self, other):
    return self.name == other.name and self.age == other.age
  
P1 = Person('Bibhu', 23)
P2 = Person('Dutta', 27)
P3 = Person('Bibhu', 23)

print(P1 == P2)
print(P1 == P3)