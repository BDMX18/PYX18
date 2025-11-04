'''
           *
           **
           ***
           ****
'''

n = int(input('Enter The Number Of Rows: '))
pattern = 1
for row in range(1, n+1):
  for pa in range(1, pattern+1):
    print('*', end='')
  print()
  pattern += 1

print('-'*30)

for row in range(1, n+1):
  for col in range(1, row+1):
    print('*', end='')
  print()