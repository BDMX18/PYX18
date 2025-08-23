n = int(input('Enter The Number Of Rows: '))
num = n
for row in range(1, n+1):
  for col in range(n, row-1, -1):
    print(f'{num} ', end='')
  print()
  num -= 1

'''
5 5 5 5 5 
4 4 4 4
3 3 3
2 2
1
'''