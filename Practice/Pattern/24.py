'''
Enter the row size for the pattern: 5
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
'''

n = int(input('Enter The Number Of Rows: '))
pattern = 1
space = n*2-2
for row in range(n*2):
  for pa in range(1, pattern+1):
    print('*', end='')
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print('*', end='')
  print()
  if(row < (n*2)//2-1):
    pattern += 1
    space -= 2
  elif(row >= (n*2)//2):
    pattern -= 1
    space += 2


