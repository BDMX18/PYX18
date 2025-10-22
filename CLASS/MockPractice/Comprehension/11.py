'''
Set Comprehension Questions

Question 11:
Given a list of numbers, create a set of their squares.

numbers = [1, 2, 2, 3, 4, 4, 5]
'''

numbers = [1, 2, 2, 3, 4, 4, 5]

op_set = {num**2 for num in numbers}

print(op_set)