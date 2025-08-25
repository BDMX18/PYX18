n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  for col in range(1, row+1):
    if((row+col)%2 == 0):
      print('1 ', end='')
    else:
      print('0 ', end='')
  print()
