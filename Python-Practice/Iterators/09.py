'''
Q9. Create a SkipIterator That Skips Every N Elements

Problem:
Given a list and a skip value, return only every N-th element.

Sample Input:

itr = SkipIterator([10,20,30,40,50,60], 2)


Expected Output:

10
30
50
'''

ip_list = eval(input('Enter A List: '))
skip_value = int(input('Enter The Skip Value: '))

class SkipIterator:

  def __init__(self, ip_list, skip_value):
    if skip_value < 1:
      raise ValueError('Skip Value Must Be Atleast 1!')
    self.ip_list = ip_list
    self.skip_value = skip_value
  
  def __iter__(self):
    self.start = 0
    return self
  
  def __next__(self):
    if self.start >= len(self.ip_list):
      raise StopIteration
    result = self.ip_list[self.start]
    self.start += self.skip_value
    return result
  

SI = SkipIterator(ip_list, skip_value)

for value in SI:
  print(value)

