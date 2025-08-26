'''
1 2 3 4 5
2       4
3       3
4       2
5 4 3 2 1

1 2 3 4 5 6 7
2           6
3           5
4           4
5           3
6           2
7 6 5 4 3 2 1
'''

n = int(input('Enter The Number Of Rows: '))
space = n - 2
for row in range(1, n + 1):
    if row == 1:
        for num in range(row, n + 1):
            print(num, end=' ')
        print()
    elif row > 1 and row < n:
        print(row, end=' ')
        for sp in range(space):
            print(' ', end=' ')
        print((n + 1) - row)
    elif row == n:
        for num in range(row, 0, -1):
            print(num, end=' ')





