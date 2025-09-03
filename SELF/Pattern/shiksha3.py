'''
0
0 1
0 2 4
0 3 6 9 
0 4 8 12 16
0 5 10 15 20 2
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(0, n):
  num = 0
  for col in range(0, row+1):
    print(num, end=' ')
    num += row
  print()