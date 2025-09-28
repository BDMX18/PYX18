'''
Enter the row size for the pattern: 4
1 
1 2 
1 2 3 
1 2 3 4 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  num = 1
  for col in range(1, row+1):
    print(num, end=' ')
    num += 1
  print()