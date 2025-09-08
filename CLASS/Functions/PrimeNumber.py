# Prime numbers between a given range.

def isPrime(num):
  if num > 1:
    for div in range(2, num//2+1):
      if(num%div == 0):
        return False
    else:
      return True
  else:
    return False
  
def primeNumbers(lr, ur):
  for num in range(lr, ur+1):
    if isPrime(num):
      print(num)

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
primeNumbers(lr, ur)