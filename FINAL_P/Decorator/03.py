'''
Argument Logging Decorator:
Write a decorator that logs the function name and all the arguments passed to it before executing.
'''

def decorator(func):
  def inner_func(*args):
    print('Function Name:', func.__name__)
    print('Arguements:', args)
    return func(*args)
  return inner_func

@decorator
def number(*args):
  l = []
  for num in args:
    l.append(num)
  return l

print(number(1,2,3,4,5))
