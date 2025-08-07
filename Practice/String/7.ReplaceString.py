# 7. Replace 'not'...'poor' with 'good'.

# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

string = input('Enter A String: ')
ipnot = string.find('not')
ippoor = string.find('poor')
if(ipnot < ippoor and ipnot > 0 and ippoor > 0):
  string = string.replace(string[ipnot:ippoor+len('poor')], 'good')
print(string)