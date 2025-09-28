'''
Enter the row size for the pattern: 5
    * 
   * * 
  *   * 
 *     * 
*       * 
 *     * 
  *   * 
   * * 
    * 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
inner_space = 1
outer_space = n-1
for row in range(1, n*2):
  for sp in range(1, outer_space+1):
    print(' ', end='')
  if row == 1 or row == n*2-1:
    print('*', end='')
  else:
    print('*', end='')
    for sp in range(1, inner_space+1):
      print(' ', end='')
    print('*', end='')
  print()
  if row < n:
    inner_space += 2
    outer_space -= 1
  else:
    inner_space -= 2
    outer_space += 1
