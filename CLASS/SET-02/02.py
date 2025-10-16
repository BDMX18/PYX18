'''
Find the character with the maximum frequency

Problem:
Given a string, find the character that appears most frequently.

Example:

Input → "successes"

Output → 's' (appears 4 times)
'''

ip_str = 'successes'
count_dict = {}
for ch in ip_str:
  if ch not in count_dict:
    count_dict[ch] = 1
  else:
    count_dict[ch] += 1
max = 0
max_char = ''
for item in count_dict:
  if count_dict[item] > max:
    max = count_dict[item]
    max_char = item
print('Alphabet:', max_char, 'Count:', max)
