'''
Find All Palindromic Substrings

Problem:
Given a string, print every substring that is a palindrome.

Sample Input: "abbaeae"
Expected Output:

a
b
b
a
bb
abba
a
e
a
e
'''

ip_str = "abbaeae"

length = len(ip_str)

palindrome_list = []

for start in range(length):
  for end in range(start+1, length+1):
    word = ip_str[start:end]
    if word == word[::-1]:
      if word not in palindrome_list:
        palindrome_list.append(word)

for word in palindrome_list:
  print(word)