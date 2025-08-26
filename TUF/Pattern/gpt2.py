'''
1 2 3 4 5
  2     4
    3   3
      4 2
        1
'''

n = int(input('Enter The Number Of Rows: '))
sp_one = n-3
for row in range(1, n+1):
  for sp in range(1, row):
    print(' ', end='')
  if(row == 1):
    for num in range(1, n+1):
      print(num, end='')
    print()
  elif(row > 1 and row < n):
    print(row, end='')
    for sp in range(1, sp_one+1):
      print(' ', end='')
    print(n+1-row, end='')
    print()
    sp_one -= 1
  elif(row == n):
    print('1')
  