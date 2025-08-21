'''
 * * * * * 
  * * * * 
   * * * 
    * * 
     *
'''

# Using Generic Approach: 

n = int(input('Enter The Number Of Rows: '))
star = n
space = 0
for row in range(1, n+1):
  for sp in range(1, space+1):
    print(' ', end='')
  for st in range(1, star+1):
    print('* ', end='')
  print()
  star -= 1
  space += 1
