'''
Transpose a Matrix

Write a function that takes a 2D matrix (list of lists) and returns its transpose.

Example:

matrix = [
  [1, 2, 3],
  [4, 5, 6]
]

Transpose:

[
  [1, 4],
  [2, 5],
  [3, 6]
]
'''

matrix = [
  [1, 2, 3],
  [4, 5, 6]
]

row = len(matrix)
column = len(matrix[0])

transpose = []
for j in range(column):
  new_row = []
  for i in range(row):
    new_row.append(matrix[i][j])
  transpose.append(new_row)
print(transpose)