'''
Basic Decorator:
Write a decorator that prints "Function execution started" before a function runs and "Function execution ended" after it completes.
'''

def decoratorFn(arg):
  def innerFn():
    print('Function Execution Started!')
    arg()
    print('Function Execution Ended!')
  return innerFn

@decoratorFn
def decoratedFn():
  print('Decorated Function Called!')

decoratedFn()