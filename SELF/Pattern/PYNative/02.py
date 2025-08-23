# n = int(input(': '))
# for row in range(1, n+1):
#   for col in range(1, row+1):
#     print(f'{col} ', end='')
#   print()


# Generic Approach:


n = int(input(': '))
pattern = 1
for row in range(1, n+1):
  dummy = 1
  for col in range(1, pattern+1):
    print(f'{dummy} ', end='')
    dummy += 1
  print()
  pattern += 1

'''
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''