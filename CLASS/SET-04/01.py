'''
Count occurrences of a substring in a string (without using .count())

Problem:
Count how many times a substring appears in a given string.

Example:

Input → "the three truths", Substring → "th"

Output → 3
'''

ip_str = 'the three truths'
sub_str = 'th'
count = 0
for ip in range(len(ip_str)):
  if ip_str[ip:ip+len(sub_str)] == sub_str:
    count += 1
print(count)