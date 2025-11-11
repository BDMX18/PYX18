'''
Q1. Validate Mobile Numbers

Write a program to validate Indian mobile numbers using regular expressions.
✅ Conditions:

Must start with 6, 7, 8, or 9

Must contain exactly 10 digits

Sample Data:

numbers = ["9876543210", "1234567890", "9988776655", "5678901234"]
'''

import re

numbers = ["9876543210", "1234567890", "9988776655", "5678901234"]

pattern = '^[6-9]{1}[0-9]{9}$'

for number in numbers:
  if re.findall(pattern, number):
    print(f'{number} is valid')
  else:
    print(f'{number} is invalid')