'''
Write a list comprehension that flattens a list of lists (e.g., [[1, 2], [3, 4], [5]]).
'''

numbers = [[1, 2], [3, 4], [5]]
numbers = [item for sublist in numbers for item in sublist]
print(numbers)
