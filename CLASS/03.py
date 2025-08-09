'''
INPUT: 'a3b2d4c3a4b1'
OUTPUT: 'aaabbddddcccaaaab'
'''

# Using For loop with range and CDT:

string = input('Enter A String: ')
new_string = ''
for ip in range(1, len(string), 2):
 new_string += string[ip-1]*int(string[ip])
print(new_string)

# Using while loop:

string = input('Enter A String: ')
new_string = ''
ip = 1
while ip < len(string):
  new_string += string[ip-1]*int(string[ip])
  ip += 2
print(new_string)