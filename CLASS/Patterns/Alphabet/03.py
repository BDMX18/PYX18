'''
    A
   A B
  A B C
 A B C D
A B C D E
'''

n = int(input('Enter The Number Of Rows: '))
space = n-1
pattern = 1
for row in range(1, n+1):
  alpha = 1
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print(f'{chr(64+alpha)} ', end='')
    alpha += 1
  print()
  space -= 1
  pattern += 1