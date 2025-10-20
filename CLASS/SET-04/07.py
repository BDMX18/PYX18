'''
Remove all vowels from a string

Problem:
Remove all vowels from a string and return the new string.

Example:

Input → "education"

Output → "dctn"
'''

ip_str = 'education'
new_str = ''
for ch in ip_str:
  if ch not in 'aeiou':
    new_str += ch
print(new_str)