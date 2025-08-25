# Approach 1:
n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  num = 1
  for col in range(1, row+1):
    print(f'{num} ', end='')
    num += 1
  print()

# Approach 2:
n = int(input('Enter The Number Of Rows: '))
pattern = 1
for row in range(1, n+1):
  num = 1
  for col in range(1, pattern+1):
    print(f'{num} ', end='')
    num += 1
  print()
  pattern += 1

