'''
   *
  ***
 *****
*******
'''

n = int(input('Enter The Number Of Rows: '))
pattern = 1
space = n-1
for row in range(1, n+1):
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print('*', end='')
  print()
  pattern += 2
  space -= 1