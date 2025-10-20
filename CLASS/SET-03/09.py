'''
Remove all special characters from a string

Problem:
Keep only letters, numbers, and spaces.

Example:

Input → "P@yt#ho!n 123"

Output → "Python 123"
'''

ip_str = 'P@yth#ho!n 123'
new = ''
for ch in ip_str:
  if ch.isalnum() or ch.isspace():
    new  += ch
print(new)