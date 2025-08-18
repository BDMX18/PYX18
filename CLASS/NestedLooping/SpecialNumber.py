# Check whether a number is Special Number or not.

num = int(input('Enter A Number: '))
fact_sum = 0
dummy = num
while dummy != 0:
  rem = dummy % 10
  fact = 1
  for i in range(1, rem+1):
    fact *= i
  dummy //= 10
  fact_sum += fact
if(num == fact_sum):
  print(f'{num} is a special number!')
else:
  print(f'{num} is not a special number!')

# Get Special Numbers within a given range:

lr = int(input('Enter Lower Range: '))
ur = int(input('Enter Upper Range: '))
for num in range(lr, ur+1):
  dummy = num
  fact_sum = 0
  while dummy != 0:
    rem = dummy % 10
    fact = 1
    for i in range(1, rem+1):
      fact *= i
    dummy //= 10
    fact_sum += fact
  if(fact_sum == num):
    print(fact_sum)

# Get 6th to 10th Special Number: Since there're only 4 special numbers, we'll never be able to reach the count value = 6. In that case, the program will get into an infinty loop.

num = 1
count = 0
while count < 10:
  fact_sum = 0
  dummy = num
  while dummy != 0:
    rem = dummy % 10
    fact = 1
    for i in range(1, rem+1):
      fact *= i
    fact_sum += fact
    dummy //= 10
  if(fact_sum == num):
    count += 1
    if(count > 5):
      print(num)
  num += 1