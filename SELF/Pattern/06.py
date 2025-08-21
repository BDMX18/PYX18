'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''

# Approach 01:
n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  print(' '*(n-1)+'*'*row)
  n -= 1

# Approach 02: Using Generic Approach:

n = int(input('Enter The Number Of Rows: '))
space = n-1
star = 1
for row in range(1, n+1):
  for sp in range(1, space+1):
    print(' ', end='')
  for st in range(1, star+1):
    print('*', end='')
  print()
  space -= 1
  star += 1

# Approach 3: Using nested loops

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  for col in range(1, n+1):
    if(row+col >= n+1):
      print('*', end='')
    else:
      print(' ', end='')
  print()