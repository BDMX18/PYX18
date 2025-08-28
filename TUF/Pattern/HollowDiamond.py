'''
Input: n = 5
Output:
    *    
   * *   
  *   *  
 *     * 
*       *
 *     * 
  *   *  
   * *   
    *    
'''

n = int(input('Enter The Number Of Rows: '))
space = n-1
space_i = 1
for row in range(1, n*2):
  for sp in range(1, space+1):
    print(' ', end='')
  print('*', end='')
  if(row < n):
    space -= 1
  else:
    space += 1
  if(row > 1 and row < n*2-1):
    for sp in range(1, space_i+1):
      print(' ', end='')
    print('*', end='')
    if(row < n):
      space_i += 2
    else:
      space_i -= 2
  print()
