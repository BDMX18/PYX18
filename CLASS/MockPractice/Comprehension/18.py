'''
Question 3:
Create a list of squares for numbers from 1 to 20 excluding numbers divisible by 3 or 5.

numbers = list(range(1, 21))
'''

op_list = [num**2 for num in range(1, 21) if num%3!=0 and num%5!=0]

print(op_list)