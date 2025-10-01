'''
Print a Multiplication Table

Write a program that prints the multiplication table from 1 to 10.

Example output:

1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
...
10 20 30 40 50 60 70 80 90 100
'''

print('Multiplication Table From 1 to 10')
for i in range(1, 11):
  print(f'\nMultplication Table of {i}')
  for j in range(1, 11):
    print(f'{i} X {j} = {i*j}')

