# 6. Add ing or ly to a string.

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

string = input('Enter A String: ')
if(len(string) > 2):
  if(string[-3:] == 'ing'):
    string += 'ly'
  else:
    string += 'ing'
print(string)