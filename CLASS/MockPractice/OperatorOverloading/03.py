'''
Overload __str__ and __repr__
Create a class Book that displays book details in a formatted way when printed.
'''

class Book:

  def __init__(self, bname, bauthor, bprice):
    self.bname = bname
    self.bauthor = bauthor
    self.bprice = bprice

  def __str__(self):
    return f'{self.bname, self.bauthor, self.bprice}'
  
  def __repr__(self):
    return f'{self.bname} {self.bauthor} {self.bprice}'

B1 = Book('Blossoms', 'Ruskin Bond', 2893)

print(B1.__str__())
print(B1.__repr__())