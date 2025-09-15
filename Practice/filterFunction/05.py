'''
Filter numbers divisible by 3 and 5.
From a list of integers, return only those divisible by both 3 and 5.
numbers = [10, 15, 30, 45, 22, 9, 75, 100]
'''

numbers = [10, 15, 30, 45, 22, 9, 75, 100]
print(list(filter(lambda x: x%3==0 and x%5 == 0, numbers)))