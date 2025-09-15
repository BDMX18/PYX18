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
'''

# n = int(input('Enter The Number Of Rows: '))
# outer_space = n-1
# inner_space = 0
# for row in range(1, n*2):
#   for sp in range(1, outer_space+1):
#     print(' ', end='')
#   print('*', end='')
#   if row != 1 and row != n*2-1:
#     for sp in range(1, inner_space+1):
#       print(' ', end='')
#     print('*', end='')
#   print()
#   if row < n:
#     outer_space -= 1
#     inner_space += 2
#   else:
#     outer_space += 1
#     inner_space -= 2