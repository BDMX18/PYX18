'''
Q4. Find all digits present in a string.
Sample Data:

text = "My phone number is 9876543210 and pin code is 760010."
'''


text = "My phone number is 9876543210 and pin code is 760010."

import re

print(re.findall('[0-9]', text))