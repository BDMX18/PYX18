'''
Write a list comprehension to create a list of numbers from 1 to 20, but only include numbers divisible by 3.
'''

list = [item for item in range(1, 21) if item%3 == 0]
print(list)