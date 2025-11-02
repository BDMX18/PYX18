'''
Count Words Without split():
Write a program to count how many words are in a given sentence without using the built-in split() function.
'''

ip_str = 'Python is an amazing language'

word = 1
for ch in ip_str:
  if ch.isspace():
    word += 1
print('Total Words:', word)