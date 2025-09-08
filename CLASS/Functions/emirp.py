# WAP to print EMIRP numbers between a given range

def isPrime(num):
  if(num > 1):
    for div in range(2, num//2+1):
      if(num % div == 0):
        return False
    else:
      return True
  else:
    return False

def reverse(num):
  reverse = 0
  while num > 0:
    rem = num % 10
    reverse = reverse*10 + rem
    num //= 10
  return reverse

def EMIRP(lr, ur):
  for num in range(lr, ur+1): 
    rev = reverse(num)
    if(rev != num):
      if(isPrime(num)):
        if(isPrime(rev)):
          print(num)

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
EMIRP(lr, ur)