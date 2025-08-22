'''
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  num = row
  for col in range(1, row+1):
    print(f'{num} ', end='')
    num += row
  print()