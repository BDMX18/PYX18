'''
Global Counter

Write a program that uses a global variable as a counter.

Define a global variable counter = 0.

Create a function increment() that increases the value of counter by 1 each time it is called.

Print the value of counter before and after calling increment() multiple times.

Hint: You will need to use the global keyword inside the function.
'''

counter = 0

def increment():
  global counter
  counter += 1

for i in range(10):
  print(f'Value Of Counter Before calling {increment.__name__} is {counter}')
  increment()
  print(f'Value Of Counter After calling {increment.__name__} is {counter}')