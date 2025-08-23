'''
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
'''

n = int(input('Enter The Number Of Rows: '))
space = n-1
pattern = 1
for row in range(1, n+1):
  num = 1
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print(f'{num} ', end='')
    num += 1
  print()
  pattern += 2
  space -= 1