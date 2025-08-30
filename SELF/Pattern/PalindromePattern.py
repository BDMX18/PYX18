'''
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1
'''

n = int(input('Enter The Number Of Rows: '))
pattern = 1
for row in range(1, n+1):
  num = 1
  for col in range(1, pattern+1):
    print(num, end=' ')
    if(col < pattern//2+1):
      num += 1
    else:
      num -= 1
  print()
  pattern += 2
    