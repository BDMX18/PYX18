'''
Question:
Write a decorator @log_call that prints the name of the function being called and its arguments.

Example:

@log_call
def greet(name):
    return f"Hello, {name}!"

greet("Alice")


Output:

Calling function: greet with arguments: ('Alice',)
'''

def log_call(arg):
  def innerFunction(*args):
    print(f'Calling Function: {arg.__name__} with arguements: {(args)}')
    return arg(*args)
  return innerFunction


@log_call
def greet(name):
  return f'Hello, {name}'

result = greet('Alice')
print(result)