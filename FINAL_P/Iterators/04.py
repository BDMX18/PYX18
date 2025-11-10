'''
Q3. Infinite Fibonacci Iterator

Problem Statement:
Create a class FibonacciIterator that generates Fibonacci numbers infinitely (until manually stopped using break).

Sample Data:

fib = FibonacciIterator()


Expected Behavior:
First few iterations should yield: 0, 1, 1, 2, 3, 5, 8, 13, ...
'''

class FibonacciIterator:

  def __init__(self):
    self.a, self.b = 0, 1

  def __iter__(self):
    return self
  
  def __next__(self):
    result = self.a
    self.a, self.b = self.b, self.a + self.b
    return result

fib = FibonacciIterator()

for value in fib:
  print(value)
  if value == 13:
    break


