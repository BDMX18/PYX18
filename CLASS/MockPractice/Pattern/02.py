'''
Hourglass Star Pattern

Print a hollow hourglass made of stars (*) with dynamic size n.

Example (n=5):

* * * * *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
* * * * *
'''

n = int(input('Enter The Number Of Rows: '))
inner_space = n
outer_space = 1
for row in range(1, n*2):
  if(row == 1 or row == n*2-1):
    print('* '*n)
  else:
    for sp in range(1, outer_space+1):
      print(' ', end='')
    print('*', end='')
    for sp in range(1, inner_space+1):
      print(' ', end='')
    if row != n:
      print('*', end='')
    print()
    if row < n:
      outer_space += 1
      inner_space -= 2
    else:
      outer_space -= 1
      inner_space += 2
