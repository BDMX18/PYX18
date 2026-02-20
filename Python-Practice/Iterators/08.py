'''
10. Skip Iterator

Create an iterator that returns every nth value from a list. Example:
List: [10,20,30,40,50], n = 2 → 10, 30, 50
'''

class SkipIterator:

  def __init__(self, list, n):
    self.list = list
    self.n = n
  
  def __iter__(self):
    self.i = 0
    return self
  
  def __next__(self):
    while self.i < len(self.list):
      result = self.list[self.i]
      self.i += 1
      if((self.i-1)%self.n != 0):
        return result
    raise StopIteration

SI = SkipIterator([10,20,30,40,50], 2)

for value in SI:
  print(value)