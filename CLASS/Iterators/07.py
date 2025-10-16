'''
Intermediate Level

Reverse Iterator
Write a custom iterator ReverseList that iterates over a list in reverse order.
'''

class ReverseIterator:

  def __init__(self, L):
    self.L = L
  
  def __iter__(self):
    self.i = -1
    return self
  
  def __next__(self):
    if(self.i >= -(len(self.L))):
      result = self.L[self.i]
      self.i -= 1
      return result
    raise StopIteration

RIO = ReverseIterator([1,2,3,4,5,6])
for index in RIO:
  print(index)