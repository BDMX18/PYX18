'''
Character Iterator
Build an iterator CharIterator that iterates through each character of a string, one by one.
'''

class CharIterator:

  def __init__(self, string):
    self.string = string

  def __iter__(self):
    self.i = 0
    return self
  
  def __next__(self):
    if(self.i < len(self.string)):
      result = self.string[self.i]
      self.i += 1
      return result
    raise StopIteration

CIO = CharIterator('Bibhu Dutta')

for ch in CIO:
  print(ch)