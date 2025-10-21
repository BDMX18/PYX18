'''
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''

n = int(input('Enter The Number Of Rows: '))
outer_space = n*2-2
pattern = 1
for row in range(1, n+1):
  num = 1
  for sp in range(1, outer_space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print(num, end=' ')
    if pa < pattern//2+1:
      num += 1
    else:
      num -= 1
  print()
  outer_space -= 2
  pattern += 2
