'''
1 2 3 4 5
1 3 5 7 9
1 4 7 10 13
1 5 9 13 17
1 6 11 16 21
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  dummy = 1
  for col in range(1, n+1):
    print(f'{dummy} ', end='')
    dummy += row
  print()