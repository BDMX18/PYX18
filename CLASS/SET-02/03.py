'''
Replace spaces with hyphens in a sentence

Problem:
Replace all spaces ' ' in a string with '-'.

Example:

Input → "Python is fun"

Output → "Python-is-fun"
'''

string = input('Enter A String: ')
op_string = ''
for ch in string:
  if ch not in ' ':
    op_string += ch
  else:
    op_string += '-'
print(op_string)