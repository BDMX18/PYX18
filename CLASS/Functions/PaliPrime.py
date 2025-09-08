# WAP to print all the paliprime numbers witin a given range

def isPrime(num):
  if num > 1:
    for div in range(2, num//2+1):
      if(num%div == 0):
        return False
    else:
      return True
  else:
    return False

def reverse(num):
  rev = 0
  while num > 0:
    rem = num % 10
    rev = rev*10 + rem
    num //= 10
  return rev

def paliPrime(lr, ur):
  for num in range(lr, ur+1):
    rev = reverse(num)
    if(rev == num and isPrime(num)):
      print(num)

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
paliPrime(lr, ur)