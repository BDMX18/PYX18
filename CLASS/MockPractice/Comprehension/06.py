'''
Dictionary Comprehension Questions

Question 6:
Create a dictionary where keys are numbers from 1 to 10 and values are their cubes.

numbers = list(range(1, 11))
'''

op_dict = {k:k**3 for k in range(1, 11)}
print(op_dict)