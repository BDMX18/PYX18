'''
Question 5:
Write a decorator check_positive that ensures all numeric arguments passed to a function are positive. If not, print an error message and do not call the function.
'''

def check_positive(func):
  def wrapper(*args):
    for num in args:
      if not isinstance(num, (float, int)):
        print(num, 'Is Not A Number!')
        return
      elif(num <= 0):
        print(num, 'Less Than Or Equal To Zero!')
        return
    return func(*args)
  return wrapper

@check_positive
def decorated(*nums):
  return [num for num in nums]

print(decorated(10, 11, 12, 17, 9.23))
    