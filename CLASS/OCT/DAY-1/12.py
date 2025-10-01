'''
Count Function Calls

Question:
Create a decorator @count_calls that counts and prints how many times a function has been called.

Example:

@count_calls
def say_hello():
    print("Hello!")

say_hello()
say_hello()


Output:

Call 1
Hello!
Call 2
Hello!
'''

def count_calls(arg):
  count = 1
  def innerFunction():
    nonlocal count
    print(f'Call {count}')
    arg()
    count += 1
  return innerFunction


@count_calls
def say_hello():
  print('Hello!')

say_hello()
say_hello()