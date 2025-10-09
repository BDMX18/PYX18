'''
9. Remove all falsy values (None, 0, False, '', etc.) from a list.
Input: [0, 1, False, 2, '', 3, None, 4]

Output: [1, 2, 3, 4]
'''

ip_list = [0, 1, False, 2, '', 3, None, 4]
op_list = []
for element in ip_list:
  if bool(element) == True:
    op_list.append(element)

print(op_list)
