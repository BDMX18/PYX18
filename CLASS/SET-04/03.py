'''
Reverse words in a sentence

Problem:
Reverse the order of words in a sentence (not the words themselves).

Example:

Input → "Python is fun"

Output → "fun is Python"
'''

ip_str = input('Enter The Input String: ')
reverse_str = ''
rev_word = ''
for ip in range(-1, -len(ip_str)-1, -1):
  if ip_str[ip].isalpha():
    rev_word += ip_str[ip]
  if ip_str[ip].isspace() or ip == -len(ip_str):
    reverse_str += rev_word[::-1]+ ' '
    rev_word = ''
print(reverse_str)