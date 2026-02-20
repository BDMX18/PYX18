'''
Q1. Create a Range Iterator (Custom Implementation of Python's Range)

Problem:
Create a custom iterator class MyRange that mimics Python’s built-in range(start, stop, step).

Requirements:

Should support positive and negative steps

Should raise StopIteration correctly

Should work in a for-loop

Sample Input:

for i in MyRange(1, 10, 2):
    print(i)


Expected Output:

1
3
5
7
9
'''

class MyRange:

  def __init__(self, start, stop, step):
    self.start = start
    self.stop = stop
    self.step = step
  
  def __iter__(self):
    self.i = self.start
    return self
  
  def __next__(self):
    if self.i < self.stop:
      result = self.i
      self.i += self.step
      return result
    else:
      raise StopIteration

MR = MyRange(1, 10, 1)

for value in MR:
  print(value)