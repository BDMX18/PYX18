# 14. Sort distinct words in comma-separated input.
# Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

string = input('Enter A String: ')
list = string.split(', ')
print(sorted(set(list)))
