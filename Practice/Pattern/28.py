'''
Enter the row size for the pattern: 4
1 0 1 0 
0 1 0 1 
1 0 1 0 
0 1 0 1 
=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  for col in range(1, n+1):
    if (row+col)%2 == 0:
      print('1', end=' ')
    else:
      print('0', end=' ')
  print()