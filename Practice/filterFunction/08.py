'''
Filter prime numbers.
From a list of integers, return only the prime numbers.
'''
numbers = [2, 3, 4, 5, 10, 13, 17, 18, 19, 20, 21]

def isPrime(num):
  if num > 1:
    for div in range(2, num//2+1):
      if(num%div == 0):
        return False
    else:
      return True
  else:
    return False
  
print(list(filter(isPrime, numbers)))