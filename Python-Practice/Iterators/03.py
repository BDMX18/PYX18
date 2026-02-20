'''
Q2. Create an Iterator That Iterates Over File in Reverse (Line-by-Line)

Problem:
Write a custom iterator ReverseFileIterator that reads a file from last line to first line.

Sample Data (file.txt):

A
B
C
D


Expected Iteration Output:

D
C
B
A
'''

with open('Alphabet.txt', 'w') as FO:
  FO.writelines(['A\n', 'B\n', 'C\n', 'D\n', 'E\n'])

class ReverseFileIterator:

  def __init__(self, filename):
    self.filename = filename
    self.data = None
    self.index = None

  def __iter__(self):
    try:
      with open(self.filename, 'r') as FO:
        self.data = FO.readlines()
        self.index = len(self.data) - 1
    except FileNotFoundError as error:
      print(error)
    return self
  
  def __next__(self):
    if self.index < 0:
      raise StopIteration
    else:
      result = self.data[self.index]
      self.index -= 1
      return result

RFI = ReverseFileIterator('Alphabet.txt')

for line in RFI:
  print(line)
