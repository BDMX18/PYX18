'''
Count occurance of a specific character in a string.
Write a program to count the occurance of character 's' in the string 'success'.
Input: success
Output: s: 3
'''

string = input('Enter A String: ')
ip = 0
count = 0
while ip < len(string):
  if(string[ip] == 's'):
    count += 1
  ip += 1
print('s: ', count)