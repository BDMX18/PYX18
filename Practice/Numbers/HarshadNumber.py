# An integer which is divisible by sum of its digits (24 => 2+4 => 6 => 24/6 = 0)

# WAP to check whether a given number is Harshad/Niven Number or not.

num = int(input('Enter A Number: '))
dummy = num
sum = 0
while dummy != 0:
  rem = dummy % 10
  sum += rem
  dummy //= 10
if (num % sum == 0):
  print('Harshad Number')
else:
  print('Not a Harshad Number')

# WAP to find all harshard numbers within a given range

ll = int(input('Enter Lower Limit: '))
ul = int(input('Enter Upper Limit: '))
for num in range(ll, ul+1):
  dummy = num
  sum = 0
  while dummy > 0:
    rem = dummy % 10
    sum += rem
    dummy //= 10
  if(num % sum == 0):
    print(num)

# Using nested-while loop, every alternate harshad number

ll = int(input('Enter Lower Limit: '))
ul = int(input('Enter Upper Limit: '))
count = 0
num = ll
while num <= ul:
  dummy = num
  d_sum = 0
  while dummy != 0:
    rem = dummy % 10
    d_sum += rem
    dummy //= 10
  if(num % d_sum == 0):
    count += 1
    if(count % 2 == 0):
      print(num)
  num += 1

# 6th to 10th Harshad Number.

num = 12
count = 1
while count < 10:
  dummy = num
  sum = 0
  while dummy != 0:
    rem = dummy % 10
    sum += rem
    dummy //= 10
  if(num % sum == 0):
    count += 1
    if(count > 5):
      print(num)
  num += 1

# First n Harshad Numbers:

n = int(input('Enter The Target: '))
num = 1
count = 0
while count < n:
  dummy = num
  d_sum = 0
  while dummy != 0:
    rem = dummy % 10
    d_sum += rem
    dummy //= 10
  if(num % d_sum == 0):
    count += 1
    print(count, num)
  num += 1
