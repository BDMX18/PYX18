'''
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6
0 1 2 3 4 5 
0 1 2 3 4
0 1 2 3
0 1 2
0 1
'''

n = int(input('Enter The Number Of Rows: '))
pattern = n+1
for row in range(1, n+1):
  num = 0
  for pa in range(1, pattern+1):
    print(num, end=' ')
    num += 1
  print()
  pattern -= 1