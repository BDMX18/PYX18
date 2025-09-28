'''
Enter the row size for the pattern: 5
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
pattern = n
for row in range(1, n+1):
  num = 1
  for pa in range(pattern, 0, -1):
    print(num, end=' ')
    num += 1
  print()
  pattern -= 1