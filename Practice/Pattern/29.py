'''
Enter the row size for the pattern: 5
*       * 
  *   *   
    *     
  *   *   
*       * 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  for col in range(1, n+1):
    if row == col or row+col == n+1:
      print('*', end='')
    else:
      print(' ', end='')
  print()