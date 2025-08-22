'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  dummy = 1
  for col in range(1, n+1):
    print(dummy, end='')
    dummy += 1
  print()