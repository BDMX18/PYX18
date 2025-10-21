'''
    1
   1 2
  1   3
 1     4
1 2 3 4 5
'''

n = int(input('Enter The Number Of Rows: '))
outer_space = n-1
inner_space = -1
for row in range(1, n+1):
  num = 1
  for op in range(1, outer_space+1):
    print(' ', end='')
  if row == 1 or row == n:
    for i in range(1, row+1):
      print(i, end=' ')
  else:
    print(num, end='')
    for ip in range(1, inner_space+1):
      print(' ', end='')
    print(row, end='')
  print()
  outer_space -= 1
  inner_space += 2