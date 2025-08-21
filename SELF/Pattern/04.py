'''
* * * * *
* * * * *
* * * * * 
* * * * * 
* * * * *
'''

# Approach 01:

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  print('* '*n)

# Approach 2: Using Nested Looping Statements:

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  for col in range(1, n+1):
    print('* ', end='')
  print()

# Approach 3: Using Generic Approach:

n = int(input('Enter The Number Of Rows: '))
star = n
for row in range(1, n+1):
  for st in range(1, star+1):
    print('*', end='')
  print()