'''
Q7. Extract Dates from String Using Regex

Write a Python program to extract all dates from a text in the format DD-MM-YYYY.

Sample Data:

text = "My birthday is on 09-10-2001 and my sister’s is on 12-12-2004."


Expected Output:

['09-10-2001', '12-12-2004']
'''

text = "My birthday is on 09-10-2001 and my sister’s is on 12-12-2004."

pattern = r'\d{2}-\d{2}-\d{4}'

import re

date = re.findall(pattern, text)

print(date)