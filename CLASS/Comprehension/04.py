'''
Flatten a 2D list [[1, 2], [3, 4], [5, 6]] into a single list using list comprehension.
'''

ip_list = [[1, 2], [3, 4], [5, 6]]
op_list = [element for sub_list in ip_list for element in sub_list]
print(op_list)