n = int(input('Enter The Number Of Rows: '))
space = n-1
star = 1
for row in range(1, n+1):
  for st in range(1, star+1):
    print('*', end='')
  for sp in range(1, space+1):
    print(' ', end='')
  for st in range(1, star+1):
    print('*', end='')
  print()
  if(row <= n//2):
    star += 1
    space -= 2
  else:
    space += 2
    star -= 1