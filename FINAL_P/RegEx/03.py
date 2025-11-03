'''
Q3. Write a regex to find all words that start with a capital letter.
Sample Data:

text = "Python is a Great Language and Easy To Learn."
'''

import re

text = "Python is a Great Language and Easy To Learn."

print(re.findall('[A-Z][a-zA-Z]+', text))