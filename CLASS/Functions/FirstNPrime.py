def isPrime(target):
  count = 0
  num = 2
  while count != target:
    for div in range(2, num//2+1):
      if(num%div == 0):
        return False
    else:
      return True
  num += 1
  count += 1

target = int(input('Enter The Target: '))

