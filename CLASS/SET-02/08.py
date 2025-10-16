'''
Find the longest word in a sentence

Problem:
Given a sentence, find and return the longest word.

Example:

Input → "Python makes coding enjoyable"

Output → "enjoyable"
'''

ip_list = "Python makes coding enjoyable"
str_list = ip_list.split()
max = 0
longest = ''
for word in str_list:
  if len(word) > max:
    max =  len(word)
    longest = word
print(longest)
