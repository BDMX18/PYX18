'''
A B C D E
A B C D E 
A B C D E
A B C D E
A B C D E
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  alpha = 1
  for col in range(1, n+1):
    print(f'{chr(64+alpha)} ', end='')
    alpha += 1
  print()