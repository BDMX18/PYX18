'''
Print a pyramid pattern of stars

Problem:
For n = 5, print the following pattern:

    *
   ***
  *****
 *******
*********
'''

n = int(input('Enter The Number Of Lines: '))
space = n-1
pattern = 1
for i in range(1, n+1):
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print('*', end='')
  print()
  space -= 1
  pattern += 2
  