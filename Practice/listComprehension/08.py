'''
Given a list of integers, write a list comprehension that replaces all negative numbers with 0.
'''

numbers = [5, -3, 8, -1, 0, -7, 12]
numbers = [item if item > 0 else 0 for item in numbers]
print(numbers)