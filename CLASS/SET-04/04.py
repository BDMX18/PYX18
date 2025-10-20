'''
Rotate a list to the right by k positions

Problem:
Rotate a list by k positions to the right.

Example:

Input → [1, 2, 3, 4, 5], k = 2

Output → [4, 5, 1, 2, 3]
'''

ip_list = eval(input('Enter A List: '))
k = int(input('Enter The Index Position: '))
op_list = ip_list[-k:] + ip_list[:-k]
print(op_list)