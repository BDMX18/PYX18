'''
Create a dictionary using comprehension that maps each number from 1 to 10 to its square.

# Expected Output:
# {1: 1, 2: 4, 3: 9, ..., 10: 100}
'''

dict2 = {num: num**2 for num in range(1, 11)}
print(dict2)