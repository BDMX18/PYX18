# # Prime Number Within A Given Range, 

# # Using For-For:

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
print(f'Prime Number(s) Between {lr} and {ur}: ', end=" ")
for num in range(lr, ur+1):
  if(num > 1):
    for div in range(2, num//2+1):
      if(num%div == 0):
        break
    else:
      print(num, end=" ")

# # Using For-While:

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
print(f'Prime Number(s) Between {lr} and {ur}: ', end=" ")
for num in range(lr, ur+1):
  if(num > 1):
    div = 2
    while(div < num//2+1):
      if(num%div == 0):
        break
      div += 1
    else:
      print(num, end=" ")

# # Using While-For:

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
print(f'Prime Number(s) Between {lr} and {ur}: ', end=" ")
num = lr
while(num <= ur):
  if(num > 1):
    for div in range(2, num//2+1):
      if(num%div == 0):
        break
    else:
      print(num, end=" ")
  num += 1

# Using While-While:

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
print(f'Prime Number(s) Between {lr} and {ur}: ', end=" ")
num = lr
while(num <= ur):
  if(num > 1):
    div = 2
    while(div < num):
      if(num%div == 0):
        break
      div += 1
    else:
      print(num, end=" ")
  num += 1

# Every Alternate Prime Number Within A Given Range:

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
count = 0
for num in range(lr, ur+1):
  if(num > 1):
    for div in range(2, num//2+1):
      if(num%div) == 0:
        break
    else:
      count += 1
      if(count%2 == 0):
        print(num)

# First Fifty Prime Numbers:

num = 2
count = 1
while count < 51:
  for div in range(2, num//2+1):
    if(num%div == 0):
      break
  else:
    print(num)
    count += 1
  num += 1

# 6th to 10th Prime Number,
 
num = 2
count = 1
while count < 10:
  for div in range(2, num//2+1):
    if(num%div == 0):
      break
  else:
    count += 1
    if(count > 5):
      print(f'{count}th Prime Number: {num}')
  num += 1

# 10th Prime Number,
 
num = 2
count = 1
while count < 10:
  for div in range(2, num//2+1):
    if(num%div == 0):
      break
  else:
    count += 1
    if(count == 10):
      print(f'{count}th Prime Number: {num}')
  num += 1