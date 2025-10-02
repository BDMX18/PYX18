'''
Filter Even Numbers
Keep only the even numbers from a list as keys, with their cubes as values.

Input: [1,2,3,4,5,6]  
Output: {2:8, 4:64, 6:216}
'''
list = [1,2,3,4,5,6]  
even_square = {num:num**3 for num in list if num % 2 == 0}
print(even_square)