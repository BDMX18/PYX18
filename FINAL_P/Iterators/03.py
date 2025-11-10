'''
Q2. Create an Iterator for a Range of Squares

Problem Statement:
Write a class SquareRange that behaves like range(), but instead of returning numbers in sequence, it returns their squares.

Sample Data:

sq = SquareRange(1, 6)


Expected Output:
When iterated: 1, 4, 9, 16, 25
'''

class SquareRange:

  def __init__(self, start, stop):
    self.start = start
    self.stop = stop
    self.current = start

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.current <= self.stop:
      result = self.current ** 2
      self.current += 1
      return result
    raise StopIteration

SR = SquareRange(1, 10)

for value in SR:
  print(value)