'''
Question 2:
Generate a list of all tuples (x, y) where x is from 1-5 and y is from 6-10 but only include tuples where x + y is even.

x_list = list(range(1, 6))
y_list = list(range(6, 11))
'''

op_list = [(x,y) for x in range(1, 6) for y in range(6, 11) if (x+y)%2==0]

print(op_list)