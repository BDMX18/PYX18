# Write a program that will find the sum of all the prime numbers between 1 to N.

def isPrime(num):
  if num > 1:
    for div in range(2, num//2+1):
      if num%div == 0:
        return False
    else:
      return True
  else:
    return False
  
def primeSum(limit):
  sum = 0
  for num in range(1, limit+1):
    if(isPrime(num)):
      sum += num
  return sum

print(primeSum(10))