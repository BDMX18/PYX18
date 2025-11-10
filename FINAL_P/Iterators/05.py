'''
Q4. Reverse String Iterator

Problem Statement:
Write an iterator class ReverseString that takes a string and iterates through it in reverse order.

Sample Data:

text = "Python"


Expected Output:
When iterated: 'n', 'o', 'h', 't', 'y', 'P'
'''

# class ReverseString:

#   def __init__(self, string):
#     self.string = string
#     self.index = len(string) - 1

#   def __iter__(self):
#     return self
  
#   def __next__(self):
#     if self.index < 0:
#       raise StopIteration
#     char = self.string[self.index]
#     self.index -= 1
#     return char

# RS = ReverseString('Python')

# for char in RS:
#   print(char)


def revStringGenerator(string):
  index = -1
  while index >= -(len(string)):
    result = string[index]
    index -= 1
    yield result

rgs = revStringGenerator('Python')

for ch in rgs:
  print(ch)