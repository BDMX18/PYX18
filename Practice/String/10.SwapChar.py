# 10. Swap first and last chars of a string.
# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

string = input('Enter A String: ')
if(len(string)>1):
  print(string[-1]+string[1:-1]+string[0])