'''
1 
3 5 
7 9 11 
13 15 17 19 
21 23 25 27 29
'''

n = int(input('Enter The Number Of Rows: '))
dummy = 1
for row in range(1, n+1):
  for col in range(1, row+1):
    print(f'{dummy} ', end='')
    dummy += 2
  print()