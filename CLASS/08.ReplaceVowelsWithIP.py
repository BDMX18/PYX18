# Using For Loop:

string = input('Enter A String: ')
new_string = ''
for ip in range(len(string)):
  if(string[ip] not in 'aeiou'):
    new_string += string[ip]
  else:
    new_string += str(ip)
print(new_string)

# Using While Loop:

string = input('Enter A String: ')
new_string = ''
ip = 0
while ip < len(string):
  if(string[ip] not in 'aeiou'):
    new_string += string[ip]
  else:
    new_string += str(ip)
  ip += 1
print(new_string)