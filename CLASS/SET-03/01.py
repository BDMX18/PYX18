'''
Problem:
Write a program to count how many words are in a given sentence without using the built-in split() function.

Example:

Input → "Python is an amazing language"

Output → 5
'''

ip_str = 'Python is an amazing language'
count = 0
is_word = False
for ch in ip_str:
  if ch.isalnum():
    if not is_word:
      count += 1
      is_word = True
  else:
    is_word = False
print(count)
