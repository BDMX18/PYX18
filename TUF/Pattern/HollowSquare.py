n = int(input('Enter The Number Of Rows: '))
space = n-2
for row in range(1, n+1):
  if(row == 1 or row == n):
    for st in range(1, n+1):
      print('*', end='')
    print()
  else:
    print('*', end='')
    for sp in range(1, space+1):
      print(' ',  end='')
    print('*', end='')
    print()