'''
Basic Iterator Creation
Write a custom iterator class CountDown that takes a number n and iterates from n to 1.
'''

class CountDown:
  def __init__(self, n,  till):
    self.till = till
    self.n = n

  def __iter__(self):
    self.i = self.n
    return self
  
  def __next__(self):
    if(self.i >= self.till):
      result = self.i
      self.i -= 1
      return result
    raise StopIteration

CDO = CountDown(10, 1)
iterator = iter(CDO)
print(CDO.__next__())
print(CDO.__next__())
print(CDO.__next__())
print(CDO.__next__())
print(CDO.__next__())


