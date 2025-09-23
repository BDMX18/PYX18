'''
1. Basic Function Wrapper

Write a decorator that prints "Function is being called" before the decorated function runs.
'''

def decoratorFunc(arg):
  def wrapperFunc():
    print('Function is being called')
    # This holds the decoratedFunc function memory address, this will call the decoratedFunc()
    arg()
  return wrapperFunc # Herein, we're returning 'wrapperFunc' function memory address.

@decoratorFunc 
# decoratedFunc = decoratorFunc(decoratedFunc)

# Herein, internally we'll be having a variable by the name of 'decoratedFunc' which will call the decoratorFunc and will pass the decoratedFunc (function memory address) to it. The decoratorFunc has one arguement (arg), which holds the decoratedFunc memory address.

# decoratorFunc(decoratedFunc), Once this function complete its execution, this function will be having 'wrapperFunc' function memory address.

def decoratedFunc():
  print('This is a decorated function!')

decoratedFunc()