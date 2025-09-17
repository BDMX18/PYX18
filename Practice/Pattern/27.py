'''
Enter the row size for the pattern: 5
1 2 3 4 5 
1       5 
1       5 
1       5 
1 2 3 4 5 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
for row in range(1, n+1):
  num = 1
  for col in range(1, n+1):
    if row == 1 or row == n:
      print(num, end=' ')
      num += 1
    else:
      if num == 1 or num == n:
        print(num, end=' ')
      else:
        print(' ', end=' ')
      num += 1
  print()