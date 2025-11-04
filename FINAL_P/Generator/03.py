'''
3. Prime Generator (Range)

Write a Python program that creates a generator function that generates all prime numbers between two given numbers.
'''

def isPrime(num):
  if num > 1:
    for div in range(2, num//2+1):
      if num%div == 0:
        return False
    else:
      return True
  return False

def prime_function(ll, ul):
  for num in range(ll, ul+1):
    if isPrime(num):
      yield num

gen = prime_function(10, 30)

print(next(gen))
print(next(gen))
print('for loop used')
for num in gen:
  print(num)