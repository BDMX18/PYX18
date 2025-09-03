'''
1
3 3 
5 5 5
7 7 7 7
9 9 9 9 9
11 11 11 11 11 11
'''

n = int(input('Enter The Number Of Rows: '))
num= 1
for row in range(1, n+1):
  for col in range(1, row+1):
    print(num, end=' ')
  print()
  num += 2