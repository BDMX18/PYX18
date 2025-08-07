# Remove odd index chars from a string
# Write a Python program to remove characters that have odd index values in a given string.

string = input('Enter A String: ')
ip = 0
even_string =  ''
while ip < len(string):
  even_string += string[ip]
  ip += 2
print(even_string)