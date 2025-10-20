'''
    A
   A B
  A B C
 A B C D
A B C D E
'''

n = int(input('Enter The Number Of Rows: '))
space = n-1
for row in range(1, n+1):
  char = 1
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, row+1):
    print(f'{char(char+pa)}', end=' ')
  print()
  space -= 1