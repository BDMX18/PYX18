'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  num = n+1-row
  for col in range(5, row-1, -1):
    print(f'{num} ', end='')
    num -= 1
  print()