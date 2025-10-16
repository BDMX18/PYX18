'''
Remove all digits from a string

Problem:
Write a program to remove all numeric characters from a given string.

Example:

Input → "Pyth0n 3.9 is aw3some!"

Output → "Python . is awesome!"
'''

ip_str = "Pyth0n 3.9 is aw3some!"
op_str = ''
for ch in ip_str:
  if ch.isalpha() or ch.isspace() or ch in '.!':
    op_str += ch
print(op_str)