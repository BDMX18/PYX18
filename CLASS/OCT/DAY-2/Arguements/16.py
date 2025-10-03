'''
Function Logger

Problem: Implement logger(func,*args,**kwargs) that calls func and returns a dictionary: {'function':func.__name__,'result':...}.
Input: logger(sum_three,2,3,4)
Output: {'function':'sum_three','result':9}
'''

def logger(func, **kwargs):
  def decorator(*args):
    kwargs.update([('function', func.__name__)])
    kwargs.update([('result', func(*args))])
    return kwargs
  return decorator

@logger
def sum_three(a,b,c):
  return a+b+c

print(sum_three(1,2,3))