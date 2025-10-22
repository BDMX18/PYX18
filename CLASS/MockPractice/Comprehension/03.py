'''
Question 3:
Generate a list of tuples (number, square) for numbers between 1 and 10.

numbers = list(range(1, 11))
'''

square_list = [(num, num**2) for num in range(1, 11)]
print(square_list)