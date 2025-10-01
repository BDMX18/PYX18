'''
5️⃣ Type Checking Decorator

Question:
Create a decorator @type_check(arg_type) that ensures the first argument to the function is of a specific type. If not, print an error.

Example:

@type_check(int)
def double(x):
    return x * 2

print(double(4))      # ✅
print(double("Hi"))   # ❌


Output:

8
Bad Type
'''

def type_check(arg):
  def outerDecorator(func):
    def innerDecorator(num):
      if isinstance(num, arg):
        return func(num)
      else:
        return 'Bad Type'
    return innerDecorator
  return outerDecorator

@type_check(int)
def double(x):
  return x*2

print(double(4))
print(double('Hi'))
