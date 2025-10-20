'''
Replace all occurrences of a substring in a string (without using .replace())

Problem:
Replace all occurrences of "is" with "was".

Example:

Input → "This is history book"

Output → "Thwas was hwas book"
'''

ip_str = input('Enter The Input String: ')
replace = input('Enter The Word To Replace: ')
new = input('Enter The New Word: ')
ip = 0
op_str = ''
while ip < len(ip_str):

  if ip_str[ip:ip+len(replace)] == replace:
    op_str += new
    ip += len(replace)
  else:
    op_str += ip_str[ip]
    ip += 1
  
print(op_str)
