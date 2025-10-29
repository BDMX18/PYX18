'''
Print all prime numbers in a given range

Problem:
Print all prime numbers between 10 and 50.
'''

def isPrime(num):
  if num > 1:
    for div in range(2, num//2+1):
      if num%div == 0:
        return False
    else:
      return True
  return False

def primeNumber(lr, ur):
  prime = []
  for num in range(lr, ur+1):
    if isPrime(num):
      prime.append(num)
  return prime

lr = int(input('Enter The Lower Range: '))
ur = int(input('Enter The Upper Range: '))
print(primeNumber(lr, ur))