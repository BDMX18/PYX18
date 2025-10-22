'''
Question 14:
Generate a set of numbers divisible by both 2 and 3 from 1 to 50.

numbers = list(range(1, 51))
'''

op_set = {num for num in range(1, 51) if num%2==0 and num%3==0}

print(op_set)