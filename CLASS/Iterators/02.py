# # Create a custom iteratoor to fetch fibonacci series of first N numbers.

class FibonacciIterator:
  def __init__(self, FN, SN, N):
    self.FN = FN
    self.SN = SN
    self.N = N
  
  def __iter__(self):
    self.count = 0
    return self
  
  def __next__(self):
    if(self.count < self.N):
      if(self.count == 0):
        self.count  += 1
        return self.FN
      elif(self.count == 1):
        self.count += 1
        return self.SN
      else:
        result = self.FN + self.SN
        self.FN, self.SN = self.SN, result
        self.count += 1
        return result
    raise StopIteration
  
FIO = FibonacciIterator(1,1, 10)
for value in FIO:
  print(value)

