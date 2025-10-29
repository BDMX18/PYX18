'''
Generate Fibonacci series up to n terms

Problem:
Generate the first n terms of the Fibonacci series.

Example:

Input → 7

Output → 0 1 1 2 3 5 8
'''

n = int(input('Enter The Range: '))
a = int(input('Enter The First Value: '))
b = int(input('Enter The Second Value: '))
for i in range(n):
  if i == 0:
    print(a, end=' ')
  elif i == 1:
    print(b, end=' ')
  else:
    sum = a+b
    a, b = b, sum
    print(sum, end=' ')