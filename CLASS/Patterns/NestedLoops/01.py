'''
*
**
***
****
*****
'''

# Approach 01:
n = int(input('Enter The Number Of Rows:'))
for row in range(1, n+1):
  print('*'*row)

# Approach 02:
n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  for col in range(1, row+1):
    print("*", end='')
  print()

# Approach 03:
n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  for col in range(1, n+1):
    if(row >= col):
      print('*', end='')
    else:
      print('', end='')
  print()
