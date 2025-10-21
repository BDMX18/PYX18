'''
Add Two Complex Numbers
Create a class Complex that overloads the + operator to add two complex numbers.
'''

class Complex:

  def __init__(self, real, imag):
    self.real = real
    self.imag = imag

  def __add__(self, other):
    return Complex(self.real + other.real, self.imag + other.imag)
  
  def __str__(self):
    return f'{self.real}+{self.imag}j'

a = Complex(2,6)
b = Complex(4, 7)

print(a + b)