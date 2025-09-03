'''
12
12 10
12 10 8
12 10 8 6
12 10 8 6 4
12 10 8 6 4 2
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  num = n*2
  for col in range(1, row+1):
    print(num, end=' ')
    num -= 2
  print()