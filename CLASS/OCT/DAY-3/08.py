'''
8. Remove Duplicate Characters

Problem:
Write a function to remove duplicate characters from a string while maintaining the original order.

Example:
Input: "programming"
Output: "progamin"
'''

def remove_duplicate(ip_string):
  op_str = ''
  for ch in ip_string:
    if ch not in op_str:
      op_str += ch
  return op_str

print(remove_duplicate('programming'))