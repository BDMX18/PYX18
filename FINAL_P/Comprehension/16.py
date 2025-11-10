'''
Q5. Element-wise Addition

Problem:
Given two lists of numbers of equal length, use list comprehension with zip() to produce a list containing the sum of corresponding elements.

Sample Data:

a = [1, 2, 3]
b = [4, 5, 6]


Expected Output:

[5, 7, 9]
'''

a = [1, 2, 3]
b = [4, 5, 6]

op_list = [i+j for i,j in zip(a, b)]

print(op_list)
