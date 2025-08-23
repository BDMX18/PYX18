'''    
    A
   A B
  A B C
   A B
    A
'''

n = int(input('Enter The Number Of Rows: '))
space = n//2
pattern = 1
for row in range(1, n+1):
  alpha = 1
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print(f'{chr(alpha+64)} ', end='')
    alpha += 1
  if(row <= n//2):
    pattern += 1
    space -= 1
  else:
    pattern -= 1
    space += 1
  print()