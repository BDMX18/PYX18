'''
      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 
'''

n = int(input('Enter The Number Of Rows: '))
pattern = 1
space = n
for row in range(1, n*2):
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print('*', end='')
  print()
  if row < n*2//2:
    space -= 1
    pattern += 2
  else:
    space += 1
    pattern -= 2