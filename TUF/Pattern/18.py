n = int(input('Enter The Number Of Rows: '))
pattern = 1
for row in range(n):
  alpha = n-row
  for col in range(1, pattern+1):
    print(f'{chr(64+alpha)} ', end='')
    alpha += 1
  print()
  pattern += 1