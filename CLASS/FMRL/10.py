'''
01> Given a list of integers, use map() to create a list where each number is squared if it’s even, and cubed if it’s odd.
'''

nums = [1, 2, 3, 4, 5, 6]

op_list = list(map(lambda x: x**2 if x%2 == 0 else x ** 3, nums))
print(op_list)

