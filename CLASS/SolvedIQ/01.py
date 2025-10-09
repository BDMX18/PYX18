'''
Write a python function that will reverse a string without using the slicing operation or reverse() function.
'''

# Approach 01: Extracting the first character of the givenn string and adding it to a reverse variable:

def reverse_str_01(ip_str):
  reverse = ''
  for ch in ip_str:
    reverse = ch + reverse
  return reverse

print(reverse_str_01('Bibhu'))

# Approach 02: Extracting characters from the given string using negative index positions.

def reverse_str_02(ip_str):
  reverse = ''
  for ip in range(len(ip_str)-1, -1, -1):
    reverse += ip_str[ip]
  return reverse

print(reverse_str_02('Dutta'))