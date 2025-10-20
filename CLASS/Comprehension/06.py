'''
Given nums = [10, 25, 30, 45, 50], use list comprehension to create a list of numbers divisible by both 5 and 10.
'''

nums = [10, 25, 30, 45, 50]

op_list = [element for element in nums if element%5== 0 and element%10==0]

print(op_list)