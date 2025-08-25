n = int(input('Enter The Number Of Rows: '))
star = 1
for row in range(1, n+1):
  for st in range(1, star+1):
    print('*', end='')
  print()
  if(row <= n//2):
    star += 1
  else:
    star -= 1