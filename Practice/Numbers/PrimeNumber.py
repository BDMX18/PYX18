# A nnumber which is divisible by 1 and itself is a prime number.

# WAP to check whether a number is prime or not.

num = int(input('Enter A Number: '))
if(num <= 1):
  print('Not A Prime Number')
else:
  for div in range(2, num//2+1):
    if(num%div == 0):
      print('Not A Prime Number')
      break
  else:
    print('Prime Number')

# Prime Numbers within a given range

ll = int(input('Enter Lower Limit: '))
ul = int(input('Enter Upper Limit: '))
for num in range(ll, ul+1):
  if(num > 1):
    for div in range(2, num//2+1):
      if(num % div == 0):
        break
    else:
      print(num)
  
# Every alternate prime number within a given range

ll = int(input('Enter Lower Limit: '))
ul = int(input('Enter Upper Limit: '))
num = ll
count = 0
while num <= ul:
  if(num > 1):
    for div in range(2, num//2+1):
      if(num%div == 0):
        break
    else:
      count += 1
      if(count % 2 == 0):
        print(num)
  num += 1

# First n numbers of prime number

n = int(input('Enter A Target: '))
count = 0
num = 2
while count < n:
  for div in range(2, num//2+1):
    if(num%div == 0):
      break
  else:
    count += 1
    print(num)
  num += 1

# 6th to 10th Prime Number

num = 2
count = 0
while count < 10:
  for div in range(2, num//2+1):
    if(num%div == 0):
      break
  else:
    count += 1
    if(count > 5):
      print(num)
  num += 1