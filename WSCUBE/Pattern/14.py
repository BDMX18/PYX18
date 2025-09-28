'''
Enter the row size for the pattern: 5
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
pattern = 1
space = n*2-2
for row in range(1, n+1):
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
  pattern += 2
  space -= 2