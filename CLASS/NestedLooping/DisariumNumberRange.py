# 135 = 1^1 + 3^2 + 5^3

# Using For-For:

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
print(f'Disaruium Number(s) Between {lr} and {ur}: ')
for num in range(lr, ur+1):
  sum = 0
  dummy = num
  for ele in range(len(str(num))):
    rem = dummy % 10
    sum += rem ** len(str(dummy))
    dummy //= 10
  if(sum == num):
    print(num)

# Using For-While:

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
print(f'Disaruium Number(s) Between {lr} and {ur}: ')
for num in range(lr, ur+1):
  sum = 0
  dummy = num
  while (dummy != 0):
    rem = dummy % 10
    sum += rem ** len(str(dummy))
    dummy //= 10
  if(num == sum):
    print(num)

# Every Alternate Disarium Number Within A Given Range:

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
count = 0
print(f'Disaruium Number(s) Between {lr} and {ur}: ')
for num in range(lr, ur+1):
  sum = 0
  dummy = num
  while (dummy != 0):
    rem = dummy % 10
    sum += rem ** len(str(dummy))
    dummy //= 10
  if(num == sum):
    count += 1
    if(count % 2 == 0):
      print(num)

# 6th to 10th Disarium Number:

# 10th Disarium Number:
