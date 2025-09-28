'''
Enter the row size for the pattern: 4
      1 
    1 2 1 
  1 2 3 2 1 
1 2 3 4 3 2 1 
  1 2 3 2 1 
    1 2 1 
      1 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
space = n*2-2
pattern = 1
for row in range(1, n*2):
  num = 1
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print(num, end=' ')
    if pa < pattern//2+1:
      num += 1
    else:
      num -= 1
  print()
  if row < n:
    space -= 2
    pattern += 2
  else:
    space += 2
    pattern -= 2
