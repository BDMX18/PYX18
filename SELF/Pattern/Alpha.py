'''
A 
B C 
D E F 
G H I J 
K L M N O
'''

n = int(input('Enter The Number Of Rows: '))
pattern = 1
dummy = 1
for row in range(1, n+1):
  for col in range(1, pattern+1):
    print(f'{chr(64+dummy)} ', end='')
    dummy += 1
  print()
  pattern += 1
