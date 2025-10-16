# For Iterator,

class ForIterator:
  def __init__(self, SL, EL, UP=1):
    print('__init__')
    self.SL = SL
    self.EL = EL
    self.UP = UP
  
  def __iter__(self):
    print('__iter__')
    self. i = self.SL
    return self
  
  def __next__(self):
    print('__next__')
    if self.i <= self.EL:
      result = self.i
      self.i += 1
      return result
    raise StopIteration

