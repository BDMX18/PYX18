'''
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********

'''

n = int(input('Enter The Number Of Rows: '))
space = 0
pattern = n
for row in range(1, n+1):
  for sp in range(1, space+1):
    print(' ', end='')
  for st in range(1, pattern+1):
    print('*', end='')
  print()
  if(row < n//2+1):
    space += 1
    pattern -= 2
  else:
    space -= 1
    pattern += 2

