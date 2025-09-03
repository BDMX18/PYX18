'''
1
2 3 4
5 6 7 8 9
10 11 12 13 14 15 16
17 18 19 20 21 22 23 24 25
26 27 28 29 30 31 32 33 34 35 36
'''

n = int(input('Enter The Number Of Rows: '))
num = 1
pattern = 1
for row in range(1, n+1):
  for col in range(1, pattern+1):
    print(num, end=' ')
    num += 1
  print()
  pattern += 2
