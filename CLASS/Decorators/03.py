'''
3. Decorator That Modifies Return Value

Create a decorator that adds 1 to the result of any function that returns a number.
'''

def addOuter(arg):
  def addInner():
    result = 1 + arg()
    print(result)
  return addInner

@addOuter
def decoratorFunc():
  num = int(input('Enter A Number: '))
  return num


decoratorFunc()