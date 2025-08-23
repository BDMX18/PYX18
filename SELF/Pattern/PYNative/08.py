n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  num = row
  for col in range(1, row+1):
    print(f'{num} ', end='')
    num -= 1
  print()

'''
1 
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''