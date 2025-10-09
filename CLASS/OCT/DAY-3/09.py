'''
9. Rotate String

Problem:
Given a string and a number k, rotate the string to the right by k characters.

Example:
Input: "hello", k=2
Output: "lohel"

Input: "abcdef", k=3
Output: "defabc"
'''

def rotate_str(ip_str, k):
  k = k % len(ip_str)
  return ip_str[-k:] + ip_str[:-k]

print(rotate_str('abcdef', 3))