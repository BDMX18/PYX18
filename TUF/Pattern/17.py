n = int(input('Enter The Number Of Rows: '))
space = n-1
pattern = 1
for row in range(1, n+1):
  alpha = 1
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print(f'{chr(64+alpha)}', end='')
    if (pa <= pattern//2):
      alpha += 1
    else:
      alpha -= 1
  print()
  pattern += 2
  space -= 1