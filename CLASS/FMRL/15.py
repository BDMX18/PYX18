'''
From a list of numbers, use filter() to get only the numbers that are prime.
'''

nums = [2, 3, 4, 5, 10, 11, 13, 16, 17, 20]

def isPrime(num):
  if num > 1:
    for div in range(2, num//2+1):
      if num%div == 0:
        return False
    else:
      return True
  else:
    return False

prime_list = list(filter(isPrime, nums))
print(prime_list)

op_list = list(filter(lambda num: num > 1 and all(num%div != 0 for div in range(2, num//2+1)), nums))

print(op_list)