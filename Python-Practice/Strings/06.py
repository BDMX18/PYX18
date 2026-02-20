'''
First Non-Repeating Character

Problem:
Return the first character that appears only once.

Sample Input: "swiss"
Expected Output: 'w'
'''

ip_str = input('Enter A String: ')

for ip in range(len(ip_str)):
  if ip_str[ip] not in (ip_str[ip+1:] and ip_str[:ip]):
    print('The First Character That Appears Only Once:', ip_str[ip])
    break