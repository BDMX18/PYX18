'''
Square Numbers

Create a dictionary of numbers and their squares for numbers from 1 to 5.

Input: range(1, 6)  
Output: {1:1, 2:4, 3:9, 4:16, 5:25}
'''

square_dict = {num: num*num for num in range(1, 6)}
print(square_dict)