'''
Q4. Create an Iterator for Fibonacci Numbers (Up to N Values)

Problem:
Write a class FibonacciIterator that generates the first N Fibonacci numbers.

Sample Input:

for num in FibonacciIterator(7):
    print(num)


Expected Output:

0
1
1
2
3
5
8
'''
class FibonacciIterator:

  def __init__(self, n):
    self.n = n
    self.first = 0
    self.second = 1
    self.count = 0
  
  def __iter__(self):
    self.first = 0
    self.second = 1
    return self
  
  def __next__(self):
    if self.count == self.n:
      raise StopIteration
    else:
      result = self.first
      self.first, self.second = self.second, self.first+self.second
      self.count += 1
      return result

FI = FibonacciIterator(7)

for value in FI:
  print(value)

