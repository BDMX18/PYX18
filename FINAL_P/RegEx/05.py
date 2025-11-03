'''
Q5. Check if a given string is a valid email address.
Sample Data:

emails = ["test@example.com", "hello@.com", "user.name@domain.co.in"]
'''

emails = ["test@example.com", "hello@.com", "user.name@domain.co.in"]

import re

pattern = '[a-z]+@[a-z]+.[a-z]{5}'

for mail in emails:
  if re.match(pattern, mail):
    print(mail, 'valid')
  else:
    print(mail, 'invalid')


