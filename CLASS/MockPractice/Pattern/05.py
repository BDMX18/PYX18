n = int(input('Enter The Number Of Rows: '))
space = n-1
pattern = 1
for row in range(1, n+1):
  num = 1
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print(num, end='')
    if pa < pattern//2+1:
      num += 1
    else:
      num -= 1
  print()
  space -= 1
  pattern += 2