'''
Question 1:
Given a list of numbers, create a new list containing the squares of only the even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

even_list = [num**2 for num in range(1, 11) if num%2 == 0]
print(even_list)