'''
A B C D E
B       D
C       C
D       B
E D C B A
'''

n = int(input('Enter The Number Of Rows: '))
space = n-2
for row in range(1, n+1):
  if(row == 1):
    for alpha in range(1, n+1):
      print(chr(64+alpha), end='')
    print()
  elif(row > 1 and row < n):
    print(chr(64+row), end='')
    for sp in range(1, space+1):
      print(' ', end='')
    print(chr(65+n-row), end='')
    print()
  elif(row == n):
    for alpha in range(n, 0, -1):
      print(chr(64+alpha), end='')
    print()