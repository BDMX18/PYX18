'''
Enter the row size for the pattern: 5
        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A 
  A B C D C B A 
    A B C B A 
      A B A 
        A 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
space = n-1
pattern = 1
for row in range(n*2-1):
  alpha = 1
  for sp in range(1, space+1):
    print(' ', end='')
  for pa in range(1, pattern+1):
    print(chr(64+alpha), end='')
    if pa < pattern//2+1:
      alpha += 1
    else:
      alpha -= 1
  print()
  if row < n*2//2 -1:
    space -= 1
    pattern += 2
  else:
    space += 1
    pattern -= 2

