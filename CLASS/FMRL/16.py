'''
You have a list of strings containing names. Use map() to capitalize only the first letter of each name.
'''

names = ['bibhu', 'dutta', 'mahapatra', 'alex', 'john']

op_list = list(map(lambda name: name.capitalize(), names))

print(op_list)