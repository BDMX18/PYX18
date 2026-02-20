'''
Reverse Iterator for a List

Problem:
Create a class ReverseListIterator that iterates over a list in reverse order.

Sample Data:
numbers = [10, 20, 30, 40]

Expected Output:

40
30
20
10
'''

class ReverseListIterator:

  def __init__(self, ip_list):
    self.ip_list = ip_list

  def __iter__(self):
    self.i = len(self.ip_list)-1
    return self
  
  def __next__(self):
    if self.i == -1:
      raise StopIteration
    else:
      result = self.ip_list[self.i]
      self.i -= 1
      return result

RLI = ReverseListIterator([10,20,30,40])

for value in RLI:
  print(value)