'''
String Compression

Problem:
Implement a basic string compression function using counts of repeated characters. For example, "aabcccccaaa" becomes "a2b1c5a3". If the compressed string is not shorter than the original, return the original string.

Example:
Input: "aabcccccaaa"
Output: "a2b1c5a3"

Input: "abc"
Output: "abc"
'''

def str_comp(string):
  comp_str = ''
  count = 1
  for ip in range(1, len(string)):
    if(string[ip] == string[ip-1]):
      count += 1
    else:
      comp_str += string[ip-1] + str(count)
      count = 1
    if(ip == len(string)-1):
      comp_str = comp_str + string[ip-1] + str((count))
  if not (len(comp_str) < len(string)):
    return string
  else:
    return comp_str

print(str_comp('aabcccccaaa'))
print(str_comp('abc'))

'''
a2b1c5a3
'''

str = 'a2b1c5a3'
new_str = ''
for ip in range(len(str)):
  if(str[ip].isdigit()):
    new_str += str[ip-1]*int(str[ip])
print(new_str)