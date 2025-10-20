'''
Swap case of each character in a string (without using .swapcase())

Problem:
Convert lowercase letters to uppercase and vice versa.

Example:

Input → "PyThOn"

Output → "pYtHoN"
'''

ip_str = 'PyThOn'
new = ''
for ch in ip_str:
  if ch.isupper():
    new += ch.lower()
  else:
    new += ch.upper()
print(new)