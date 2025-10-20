'''
Given a list nums = [1, 2, 3, 4, 5, 6], use a list comprehension to create a new list of only even numbers.
'''

nums = [1, 2, 3, 4, 5, 6]

op_list = [element for element in nums if element % 2 == 0]

print(op_list)