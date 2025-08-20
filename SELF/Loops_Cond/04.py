'''
4. Construct Pattern (Diamond Pattern)

Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''

n = int(input('Enter The Number Of Stars: '))
for i in range(1, n+1):
  for j in range(1, i+1):
    print('*', end='')
  print()
for i in range(n-1, 0, -1):
  for j in range(1, i+1):
    print('*', end='')
  print()