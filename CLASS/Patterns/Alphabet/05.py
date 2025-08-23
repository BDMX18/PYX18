'''
A
B C
D E F
G H I J
K L M N O
'''

n = int(input('Enter The Number Of Rows: '))
alpha = 1
for row in range(1, n+1):
  for col in range(1, row+1):
    print(f'{chr(64+alpha)} ', end='')
    alpha += 1
  print()