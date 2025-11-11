'''
Q2. Validate Email Addresses

Write a regex to validate email addresses.
✅ Must have:

Username part before '@'

A domain name after '@'

Must end with .com, .org, or .in

Sample Data:

emails = ["john@gmail.com", "user@company.org", "admin@abc.in", "test@abc"]
'''

import re

emails = ["john@gmail.com", "user@company.org", "admin@abc.in", "test@abc"]

pattern = '\w@\w\.\w'

for email in emails:
  if (re.findall(pattern, email)):
    print(f'{email} is valid!')
  else:
    print(f'{email} is invalid!')