'''
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  dummy = row
  for col in range(1, n+1):
    print(dummy, end='')
    dummy += 1
  print()