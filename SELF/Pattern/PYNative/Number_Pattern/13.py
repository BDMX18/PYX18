'''
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  num = row
  for col in range(1, n+1):
    print(num, end=' ')
    num += 1
  print()