'''
Find Longest Word:
Write a program that reads a line of text and prints the longest word in it.
'''

ip_str = input('Enter A String: ')
words = ip_str.split()
longest = words[0]
for word in words:
  if len(word) > len(longest):
    longest = word
print(longest)