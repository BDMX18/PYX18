'''
8. Convert Numbers to Strings Map
Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.

Original list and tuple:
[1, 2, 3, 4]
(0, 1, 2, 3)

List of strings:
['1', '2', '3', '4']

Tuple of strings:
('0', '1', '2', '3')
'''

print('List Of Stirng:\n',list(map(str, ['1', '2', '3', '4'])))
print('Tuple Of Stirng:\n',tuple(map(str, ['1', '2', '3', '4'])))