'''
Sum of Numbers in String:
Given a string containing numbers and alphabets, find the sum of all digits present.
'''

ip_str = 'abc12de3f4'

sum = 0

for ch in ip_str:
  if ch.isdigit():
    sum += int(ch)

print('Sum:', sum)