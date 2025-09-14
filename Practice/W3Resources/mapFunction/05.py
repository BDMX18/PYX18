'''

5. Square Elements Map: Write a Python program to square the elements of a list using the map() function.

Original List:  [4, 5, 2, 9]
Square the elements of the said list using map():
[16, 25, 4, 81]
'''

L = eval(input('Enter A List:'))
print('Original List: ', L)
print('Square the elements of the said list using map():')
print(list(map(lambda num:num**2, L)))