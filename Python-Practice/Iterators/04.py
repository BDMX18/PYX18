'''
Q3. Create an Iterator That Loops Infinitely (Circular Iterator)

Problem:
Create CircularIterator that cycles through a list forever.

Sample Input:

colors = ["red", "green", "blue"]
itr = CircularIterator(colors)


Expected Behavior:
Calling next(itr) repeatedly should output:

red
green
blue
red
green
blue
...


(Does not stop.)
'''

colors = ["red", "green", "blue"]

class CircularIterator:

  def __init__(self, colors):
    self.colors = colors
    self.i = None

  def __iter__(self):
    self.i = 0
    return self
  
  def __next__(self):
    if self.i >= len(self.colors):
      self.i = 0
    else:
      result = self.colors[self.i]
      self.i += 1
      return result
    
CI = CircularIterator(colors)

for color in CI:
  print(color)
