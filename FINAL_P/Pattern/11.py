'''
   *
  **
 ***
****
 ***
  **
   *
'''

n = int(input('Enter The Number Of Rows: '))
space = n//2
pattern = 1
for row in range(1, n+1):
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print('*', end='')
  print()
  if row <= n//2:
    space -= 1
    pattern += 1
  else:
    space += 1
    pattern -= 1