'''
    *
    *
* * * * *
    *
    *
'''

n = int(input('Enter The Number Of Rows: '))
space = n-1
pattern = n
for row in range(1, n+1):
  if row == n//2+1:
    for pa in range(1, pattern+1):
      print('*', end=' ')
  else:
    for sp in range(1, space+1):
      print(' ', end='')
    print('*', end='')
  print()