'''
    1
  1 2 3
1 2 3 4 5
  1 2 3
    1
'''

n = int(input('Enter The Number Of Rows: '))
pattern = 1
space = n//2
for row in range(1, n+1):
  num = 1
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print(f'{num}', end='')
    num += 1
  if(row <= n//2):
    pattern += 2
    space -= 1
  else:
    pattern -= 2
    space += 1
  print()