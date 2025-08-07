# 02. Count character frequency in a string.

# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

string = input('Enter A String: ').lower()
dict = {}
for char in string:
  if char in dict:
    dict[char] += 1
  else:
    dict[char] = 1
print(dict)