'''
Write a program to check if a string ends with a digit.
Sample Data:

text = "Python3"
'''

import re
text = 'Python3'
if(re.search('/d$', text)):
  print('String ends with a digit')
else:
  print('String doesn\'t ends with a digit')