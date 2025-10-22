'''
Create a decorator repeat_decorator that executes a function twice whenever it is called.
'''

def repeat_decorator(arg):
  def inner():
    arg()
    arg()
    return 'Function Executed Twice'
  return inner

@repeat_decorator
def decorated_func():
  print('Hello')

print(decorated_func())