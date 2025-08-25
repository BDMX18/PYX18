n = int(input('Enter The Number Of Rows: '))
pattern = 1
for row in range(1, n+1):
  alpha = 1
  for col in range(1, pattern+1):
    print(f'{chr(64+alpha)} ', end='')
    alpha += 1
  print()
  pattern += 1