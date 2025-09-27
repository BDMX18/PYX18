'''
Given a list of numbers, use list comprehension to create a list of factorials for each number (you may use the math.factorial function).
'''

numbers = [3, 4, 5, 6]

from math import factorial as f

numbers = [f(item) for item in numbers]
print(numbers)
