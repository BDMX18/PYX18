'''
Tuple Swap

Input:

a = (10, 20)  
b = (30, 40)


Output:

After swapping: a = (30, 40), b = (10, 20)
'''

a = (10, 20)
b = (30, 40)

a, b = b, a
print('a: ',a, 'b: ',b)