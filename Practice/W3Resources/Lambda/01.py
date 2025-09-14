'''
1. Lambda Add & Multiply
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
Sample Output:
25
48
'''

a = lambda num1: num1+15
b = lambda num1, num2: num1*num2
print(a(10), b(12, 4))