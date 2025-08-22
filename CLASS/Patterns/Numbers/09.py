'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1,  n+1):
  dummy = (n+1)-row
  for col in range(n, row-1, -1):
    print(f'{dummy} ', end='')
    dummy -= 1
  print()