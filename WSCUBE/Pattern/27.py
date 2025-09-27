'''
Enter the row size for the pattern: 5
1 2 3 4 5 
1       5 
1       5 
1       5 
1 2 3 4 5 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
space = n-2
for row in range(1, n+1):
  num = 1
  if row == 1 or row == n:
    for i in range(1, n+1):
      print(i, end='')
  else:
    print(num, end='')
    for sp in range(1, space+1):
      print(' ', end='')
    print(n, end='')
  print()

