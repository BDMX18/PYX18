'''
Question 4:
Flatten a 2D list into a 1D list.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

op_list = [element for sublist in matrix for element in sublist]
print(op_list)

