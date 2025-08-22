'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
'''

n = int(input('Enter The Number Of Rows: '))
dummy = n
for row in range(1, n+1):
  for col in range(n, row-1, -1):
    print(f'{dummy} ', end='')
  print()
  dummy -= 1