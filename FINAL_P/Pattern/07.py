'''
   *
  * *
 *   *
*******
'''

n = int(input('Enter The Number Of Rows: '))
outer_space = n-1
inner_space = 1
for row in range(1, n+1):
  for op in range(1, outer_space+1):
    print(' ', end='')
  if row == 1:
    print('*', end='')
  elif row == n:
    print('*'*(n*2-1), end='')
  else:
    print('*', end='')
    for ip in range(1, inner_space+1):
      print(' ', end='')
    print('*', end='')
  print()
  outer_space -= 1
  inner_space += 2

