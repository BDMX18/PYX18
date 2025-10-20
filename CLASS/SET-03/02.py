'''
Find the first non-repeating character in a string

Problem:
Return the first character in a string that doesn’t repeat.
If all characters repeat, return None.

Example:

Input → "aabbccdeff"

Output → 'd'
'''

ip_str = 'aabbccdeff'
occurance = dict()
count = 1
for ch in ip_str:
  if ch not in occurance:
    occurance[ch] = count
  elif ch in occurance:
    occurance[ch] += 1
for ch in ip_str:
  if occurance[ch] == 1:
    print(ch)