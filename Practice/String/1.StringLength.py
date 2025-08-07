# 01. Calculate string length: Write a Python program to calculate the length of a string.

string = input('Enter A String: ')

# Approach 01: Using Built-in Method:
print('Length Of String: ', len(string))

# Approach 02: Manual Calculation:
length = 0
for char in string:
  length += 1
print('Length Of String: ', length)


