'''
1
3 2
6 5 4
10 9 8 7
'''

n = int(input('Enter Number Of Rows: '))
for row in range(1, n+1):
  num = row*(row+1) // 2
  for col in range(1, row+1):
    print(round(num), end=' ')
    num -= 1
  print()