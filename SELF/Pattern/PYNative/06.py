n = int(input('Enter The Number Of Rows: '))
num = 1
pattern = 1
for row in range(1, n+1):
  for col in range(1, pattern+1):
    print(f'{num} ', end='')
  print()
  num += 2
  pattern += 1

'''
1 
3 3
5 5 5
7 7 7 7
9 9 9 9 9
'''