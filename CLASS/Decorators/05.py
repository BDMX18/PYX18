'''
5. Decorator with Arguments (Decorator Factory)

Create a decorator that takes an argument (e.g. a string prefix) and prints it before running the function.

Example:

@print_with_prefix(">>>")
def hello():
    print("Hello")
'''

def print_with_prefix(*args):
  def inner_func():
    for ip in args:
      result = f'{ip} {ip+1}'
    return result
  return inner_func

@print_with_prefix('>>>')
def hello():
  print('Hello')