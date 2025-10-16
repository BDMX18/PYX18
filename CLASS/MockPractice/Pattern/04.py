'''
1       9
 2     8
  3   7
   4 6
    5
'''

n = int(input('Enter The Number Of Rows: '))
inner_space = n+2
outer_space = 0
for row in range(1, n+1):
  num = row
  for sp in range(1, outer_space+1):
    print(' ', end='')
  print(num, end='')
  for sp in range(1, inner_space+1):
    print(' ', end='')
  if row != n:
   print((n*2)-num, end='')
  print()
  outer_space += 1
  inner_space -= 2
