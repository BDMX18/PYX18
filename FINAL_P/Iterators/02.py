'''Range Iterator'''

class rangeIterator:

  def __init__(self, ll, ul, up):
    self.ll = ll
    self.ul = ul
    self.up = up
  
  def __iter__(self):
    self.i = self.ll
    return self
  
  def __next__(self):
    if self.i <= self.ul:
      result = self.i
      self.i += 1
      return result
    raise StopIteration

RIO = rangeIterator(10, 20, 1)

for value in RIO:
  print(value)