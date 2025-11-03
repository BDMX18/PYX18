'''
Execution Time Decorator:
Create a decorator that measures and prints the execution time of any function it decorates.
'''

import time

def decoratorFn(arg):
  def innerFn():
    start = time.time()
    print(arg())
    end = time.time()
    result = end - start
    return round(result, 2)
  return innerFn

@decoratorFn
def decoratedFn():
  a = int(input())
  b = int(input())
  return  a + b

print(decoratedFn())