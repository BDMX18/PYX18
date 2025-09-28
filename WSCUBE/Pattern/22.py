'''
Enter the row size for the pattern: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

=== Code Execution Successful ===
'''

n = int(input('Enter The Number Of Rows: '))
num = 1
for row in range(1, n+1):
  for col in range(1, row+1):
    print(num, end=' ')
    num += 1
  print()

n = int(input('Enter The Number Of Rows: '))
pattern = 1
num = 1
for row in range(1, n+1):
  for col in range(1, pattern+1):
    print(num, end=' ')
    num += 1
  print()
  pattern += 1
