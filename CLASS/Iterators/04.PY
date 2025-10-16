'''
Even Number Iterator
Create an iterator EvenNumbers that yields even numbers starting from 2 up to a given limit.
'''

class EvenIterator:

  def __init__(self, limit, even=2):
    self.even = even
    self.limit = limit

  def __iter__(self):
    self.i = self.even
    return self
  
  def __next__(self):
    if self.limit != 0:
      result = self.even
      self.even += 2
      self.limit -= 1
      return result
    raise StopIteration

EIO = EvenIterator(10)
iterator = iter(EIO)
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())
print(EIO.__next__())