'''
Repeat Function Execution Decorator

Question:
Write a decorator @repeat(n) that executes the decorated function n times.

Example:

@repeat(3)
def laugh():
    print("Haha!")

laugh()


Output:

Haha!
Haha!
Haha!
'''

def repeat(n):
  def outerDecorator(arg):
    def innerDecorator():
      for i in range(n):
        arg()
    return innerDecorator
  return outerDecorator

@repeat(3)
def laugh():
  print('Haha!')

laugh()