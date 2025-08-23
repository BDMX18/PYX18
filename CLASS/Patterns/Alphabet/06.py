'''
A
B B
C C C
D D D D
E E E E E
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  alpha = row
  for col in range(1, row+1):
    print(f'{chr(alpha+64)} ', end='')
  print()