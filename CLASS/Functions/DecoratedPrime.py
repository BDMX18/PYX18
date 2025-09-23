from time import time as t

def decorationOuter(arg):
  def timer(LL, UL):
    start = t()
    arg(LL, UL)
    end = t()
    print('\nTime Taken:', end-start)
  return timer

@decorationOuter  
def primeNumber(LL, UL):
  for num in range(LL, UL+1):
    if num > 1:
      for div in range(2, num//2+1):
        if(num%div == 0):
          break
      else:
        print(num, end=' ')

primeNumber(10, 100)

