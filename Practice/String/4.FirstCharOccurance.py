# 4. Replace first char occurrences with $.

# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

string = input('Enter A String: ')
first_char = string[0]

# Approach 01: Using Built-in Method:
print(first_char+string[1:].replace(first_char, '$'))

# Approach 02: Manual Approach:
result_string = first_char
for char in string[1:]:
  if char == first_char:
    result_string += '$'
  else:
    result_string += char
print(result_string)