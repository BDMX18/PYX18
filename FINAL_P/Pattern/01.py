'''
           ****
           ****
           ****
           ****
'''

n = int(input('Enter The Number Of Rows: '))
for i in range(n):
  for j in range(n):
    print('*', end='')
  print()

print('-'*30)

for i in range(n):
  print('*'*n, end='')
  print()