'''
1. Triple Numbers Map

Write a Python program to triple all numbers in a given list of integers. Use Python map.
'''

num_list = eval(input('Enter A List: '))
print('Triple List: ', list(map(lambda element: element*3, num_list)))