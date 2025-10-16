'''
Diamond with Numbers

Print a diamond pattern with numbers increasing horizontally, forming a symmetric diamond.

Example (n=5):

    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
'''

n = int(input('Enter The Number Of Rows: '))
space = n-1
pattern = 1
for row in range(1, n*2):
  num = row
  for sp in range(1, space+1):
    print(' ', end='')
  for i in range(1, pattern+1):
    print(i, end=' ')
  print()
  if row < n:
    space -= 1
    pattern += 1
  else:
    space += 1
    pattern -= 1

  