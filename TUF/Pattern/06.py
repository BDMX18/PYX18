# Approach 01:
n = int(input('Enter The Number Of Rows: '))
row = 1
while row < n+1:
  num = 1
  col = 5
  while col > row-1:
    print(f'{num} ', end='')
    num += 1
    col -= 1
  print()
  row += 1

# Approach 02:
n = int(input('Enter The Number Of Rows: '))
pattern = 5
for row in range(1, n+1):
  num = 1
  for col in range(1, pattern+1):
    print(f'{num} ', end='')
    num += 1
  print()
  pattern -=1