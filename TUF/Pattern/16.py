n = int(input('Enter The Number Of Rows: '))
alpha = 1
for row in range(1, n+1):
  for col in range(1, row+1):
    print(f'{chr(alpha+64)} ', end='')
  alpha += 1
  print()