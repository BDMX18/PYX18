'''
Enter the row size for the pattern: 5
A B C D E 
A B C D 
A B C 
A B 
A 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
pattern = n
for row in range(1, n+1):
  alpha = 1
  for pa in range(pattern, 0, -1):
    print(f'{chr(alpha+64)}', end=' ')
    alpha += 1
  print()
  pattern -= 1