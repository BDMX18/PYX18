'''
Count digits, alphabets, and special characters in a string

Problem:
Determine how many digits, alphabets, and special characters are in a string.

Example:

Input → "Bibhu@123"

Output → Alphabets: 5, Digits: 3, Special: 1
'''

ip_str = 'Bibhu@123'
alpha = 0
digit = 0
special = 0
for ch in ip_str:
  if ch.isalpha():
    alpha += 1
  elif ch.isdigit():
    digit += 1
  else:
    special += 1
print(f'Alphabets: {alpha}, Digits: {digit}, Special: {special}')