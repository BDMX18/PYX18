'''
Q2. Filter Even-Indexed Elements

Problem:
Given a list of numbers, use list comprehension with enumerate() to extract only those elements that are at even indexes.

Sample Data:

nums = [10, 20, 30, 40, 50, 60]


Expected Output:

[10, 30, 50]
'''

nums = [10, 20, 30, 40, 50, 60]

op_nums = [num for i, num in enumerate(nums) if i%2==0]

print(op_nums)