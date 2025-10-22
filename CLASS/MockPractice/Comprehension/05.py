'''
Question 5:
Create a list of all prime numbers from 1 to 50.

numbers = list(range(1, 51))
'''

def isPrime(num):
  if num >= 2:
    for div in range(2, num//2+1):
      if num%div == 0:
        return False
    else:
      return True
  return False

op_list = [num for num in range(1, 51) if isPrime(num)]

print(op_list)