'''
   ****
  ****
 ****
****
'''

n = int(input('Enter The Number Of Rows: '))
space = n-1
for row in range(1, n+1):
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, n+1):
    print('*', end='')
  print()
  space -= 1
