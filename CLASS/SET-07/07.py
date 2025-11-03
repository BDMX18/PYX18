'''
Function to Check Prime Number

Input:

num = 17


Output:

17 is a prime number
'''

def isPrime(num):
  if num > 1:
    for div in range(2, num//2+1):
      if num%div==0:
        return False
    else:
      return True
  return False

num = int(input('Enter A Number: '))
if(isPrime(num)):
  print(num, 'Is A Prime Number')
else:
  print(num, 'Is Not A Prime Number')