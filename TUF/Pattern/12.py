n = int(input('Enter The Number Of Rows: '))
space = n*2-2
num = 1
for row in range(1, n+1):
  for nu in range(1, num+1):
    print(nu, end='')
  for sp in range(1, space+1):
    print(' ', end='')
  for nu in range(num, 0, -1):
    print(nu, end='')
  print()
  space -= 2
  num += 1