'''
Q8. Iterator for Prime Numbers in a Range

Problem Statement:
Write a class PrimeIterator that iterates through all prime numbers within a given range.

Sample Data:

primes = PrimeIterator(10, 30)


Expected Output:
11, 13, 17, 19, 23, 29
'''

class PrimeIterator:

  def __init__(self, start, stop):
    self.start = start
    self.stop = stop
  
  def __iter__(self):
    self.init = self.start
    return self
  
  def __next__(self):
    while self.init <= self.stop:
      num = self.init
      self.init += 1

      if num > 1:
        for div in range(2, num//2+1):
          if num % div == 0:
            break
        else:
          return num
    raise StopIteration

PI = PrimeIterator(10, 30)

for value in PI:
  print(value)