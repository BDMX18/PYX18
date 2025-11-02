'''
Remove Punctuation:
Write a Python program to remove all punctuation from a string without using any built-in methods.
'''

import re
text = 'Hello!!! How are you? I\'m fine.'
new_str = ''
for ch in text:
  if ch.lower() in 'abcdefghijklmnopqrstuvwxyz ':
    new_str += ch
print(new_str)