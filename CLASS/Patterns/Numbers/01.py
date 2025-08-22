'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''

n = int(input('Enter The Number Of Rows: '))
dummy = 1
for row in range(1, n+1):
  for col in range(1, n+1):
    print(dummy, end='')
  print()
  dummy += 1