'''
Check if a list is a palindrome

Problem:
Determine whether a list reads the same forward and backward.

Example:

Input → [1, 2, 3, 2, 1]

Output → True
'''

ip_list = [1, 2, 3, 4, 2, 1]
is_palindrome = False
for ip in range(len(ip_list)//2):
  if ip_list[ip] != ip_list[-ip-1]:
    print('List Is Not Palindrome')
    break
else:
  print('List is palindrome!')
