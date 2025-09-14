'''
2. Add Three Lists Map Lambda

Write a Python program to add three given lists using Python map and lambda.
'''

L1 = eval(input())
L2 = eval(input())
L3 = eval(input())
print('Sum Of List: ', list(map(lambda a, b, c: a+b+c, L1, L2, L3)))