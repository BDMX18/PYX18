'''
Basic Matching

Q1. Write a Python program to check if a string starts with 'Hello'.
Sample Data:

text = "Hello, welcome to Python!"
'''

import re

text = 'Hello, Welcome to Python!'

pattern = '^Hello'

print(re.findall(pattern, text))