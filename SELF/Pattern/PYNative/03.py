# Approach 1:

n = int(input())
for row in range(1, n+1):
  for col in range(n, row-1, -1):
    print(f'{row} ', end='')
  print()

# Approach 2: Generic Approach:

n = int(input(': '))
pattern = n
dummy = 1
for row in range(1, n+1):
  for col in range(1, pattern+1):
    print(f'{dummy} ', end='')
  print()
  dummy += 1
  pattern -= 1

'''
1 1 1 1 1 
2 2 2 2
3 3 3
4 4
5
'''