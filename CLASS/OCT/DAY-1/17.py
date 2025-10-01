'''
Decorator to Ensure Argument is a Positive Number

Question:
Create a decorator @positive_args that checks if all arguments passed to the function are positive numbers (ints or floats).

If any argument is non-positive or not a number, print "All arguments must be positive numbers." and do not run the function.

Otherwise, run the function normally.

Example:

@positive_args
def multiply(a, b):
    return a * b

print(multiply(3, 5))   # Should run and print 15
print(multiply(-1, 4))  # Should print the warning and not run


Expected output:

15
All arguments must be positive numbers.
'''

def positive_args(func):
  def decorator(*args):
    for arg in args:
      if not (isinstance(arg, (int, float)) and arg > 0):
        return 'All aruements must be positive numbers'
    return func(*args)
  return decorator

@positive_args
def multiply(a, b):
  return a*b

print(multiply(3, 5))
print(multiply(-1, 4))