# Approach 01:
n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  for col in range(1, row+1):
    print('*', end='')
  print()

# Approach 02:
n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  print('*'*row)