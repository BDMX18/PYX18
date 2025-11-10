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
pattern = 1
for row in range(1, n+1):
  for pa in range(1, pattern+1):
    print('*', end='')
  print()
  if row <= n//2:
    pattern += 1
  else:
    pattern -= 1
