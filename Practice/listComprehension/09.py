'''
Create a list comprehension that pairs each number in a list with its square as a tuple.
'''

numbers = [1, 2, 3, 4, 5]
numbers = [(item, item*item) for item in numbers]
print(numbers)