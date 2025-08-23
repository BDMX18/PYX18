'''
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1
  1 2 3 2 1
    1 2 1
      1
'''

n = int(input('Enter The Number Of Rows: '))
space = n//2
pattern = 1
for row in range(1, n+1):
  num = 1
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print(num,  end='')
    if pa <= pattern//2:
      num += 1
    else:
      num -= 1
  if(row <= n//2):
    space -= 1
    pattern += 2
  else:
    space += 1
    pattern -= 2
  print()