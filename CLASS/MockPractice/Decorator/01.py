'''
Write a decorator called uppercase_decorator that converts the returned string of any function into uppercase.
'''

def uppercase_decorator(arg):
  def inner():
    ip = arg()
    return ip.upper()
  return inner

@uppercase_decorator
def convert_str():
  ip_str = input('Enter A String: ')
  return ip_str

print(convert_str())