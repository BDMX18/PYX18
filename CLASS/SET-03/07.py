'''
Find all numbers that are divisible by both 3 and 5 in a given range

Problem:
Print all numbers divisible by both 3 and 5 within a given range.

Example:

Input → start = 1, end = 50

Output → [15, 30, 45]
'''

op_list = [num for num in range(1, 51) if num%3==0 and num%5==0]
print(op_list)