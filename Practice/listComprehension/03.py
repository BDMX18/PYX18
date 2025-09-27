'''
Given a list of numbers, write a list comprehension to extract only the even numbers.
'''

numbers = [3, 4, 7, 10, 15, 18, 21, 24]

numbers = [item for item in numbers if item%2 == 0]
print(numbers)

print(list(map(lambda x: x if x%2 == 0 else False, numbers)))

print(list(filter(lambda x: x%2==0, numbers)))