'''
Write a decorator that measures and prints the execution time of the function it wraps.
prime numbers within a give range
'''
import time

def isPrime(num):
  if num > 2:
    for div in range(2, num//2+1):
      if num%div == 0:
        return False
    else:
      return True
  else:
    return False

def primeDecorator(arg):
  def inner(ll, ul):
    start = time.time()
    print(arg(ll, ul))
    end = time.time()
    return end - start
  return inner
    

@primeDecorator
def primeNumber(LL, UL):
  prime_list = []
  for num in range(LL, UL+1):
    if isPrime(num):
      prime_list.append(num)
  return prime_list

print(primeNumber(1, 1000))


