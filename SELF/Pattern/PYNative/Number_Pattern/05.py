n = int(input('Enter The Number Of Rows: '))
pattern = n+1
for row in range(1, n+1):
  num = 0
  for col in range(1, pattern+1):
    print(f'{num} ', end='')
    num += 1
  print()
  pattern -= 1

'''
0 1 2 3 4 5 
0 1 2 3 4
0 1 2 3
0 1 2
0 1
'''