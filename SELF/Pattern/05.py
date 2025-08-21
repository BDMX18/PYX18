'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

# Approach 1:

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  print('*'*row, end='')
  print()

# Approach 2: Using Nested Loops:

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  for col in range(1, row+1):
    print('*', end='')
  print()

# Approach 3: Using Generic Approach:

n = int(input('Enter The Number Of Rows: '))
star = 1
for row in range(1, n+1):
  for st in range(1, star+1):
    print('*', end='')
  print()
  star += 1