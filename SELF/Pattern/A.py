'''
A 
A A 
A A A 
A A A A 
A A A A A 
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  alpha = 'A'
  for col in range(1, row+1):
    print(f'{alpha} ', end='')
  print()