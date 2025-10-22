'''
Question 4:
Create a decorator repeat(n) which repeats the execution of the decorated function n times.
👉 Example:

@repeat(3)
def say_hello():
    print("Hello")
'''

n = int(input('Enter Count: '))

def repeat(n):
  def outer_decorator(func):
    def inner_decorator():
      for i in range(n):
        func()
      return 'Executed Successfully!'
    return inner_decorator
  return outer_decorator



@repeat(n) # say_hello = repeat(say_helloFA)
def say_hello():
  print('Hello')


say_hello()