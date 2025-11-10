'''
*******
 *   *
  * *
   *
'''

n = int(input('Enter The Number Of Rows: '))
pattern = n*2-1
outer_space = 0
inner_space = n+1
for row in range(1, n+1):
  if row == 1:
    for pa in range(pattern):
      print('*', end='')
  elif row > 1 and row < n:
    for os in range(1, outer_space+1):
      print(' ', end='')
    print('*', end='')
    for ip in range(1, inner_space+1):
      print(' ', end='')
    print('*', end='')
  elif row == n:
    for os in range(1, outer_space+1):
      print(' ', end='')
    print('*', end='')
  print()
  outer_space += 1
  inner_space -= 2
