'''
Result Caching Decorator (Memoization)

Question:
Write a decorator @cache_result that caches the result of function calls so repeated calls with the same arguments don’t re-compute the result.

Example:

@cache_result
def slow_add(a, b):
    print("Calculating...")
    return a + b

print(slow_add(2, 3))
print(slow_add(2, 3))


Output:

Calculating...
5
5


(Second call doesn't print "Calculating..." because result was cached.)
'''

def cache_result(arg):
  cache = {}
  def innerFunction(*args):
    if args in cache:
      return cache[args]
    result = arg(*args)
    cache[args] = result
    return result
  return innerFunction

@cache_result
def slow_add(a, b):
  print("Calculating...")
  return a + b

print(slow_add(2, 3))
print(slow_add(2, 3))


