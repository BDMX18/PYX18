'''
Iterator with StopIteration
Create an iterator Squares that returns squares of numbers from 1 up to a given limit.
Raise StopIteration when the limit is reached.
'''

class SquareIterator:

  def __init__(self, UL, LL=1):
    self.LL = LL
    self.UL = UL
  
  def __iter__(self):
    self.i = self.LL
    return self
  
  def __next__(self):
    if(self.i <= self.UL):
      result = self.i**2
      self.i += 1
      return result
    raise StopIteration
  
SIO = SquareIterator(5)

for sq in SIO:
  print(sq)