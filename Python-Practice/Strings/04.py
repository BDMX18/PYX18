'''
Check if Two Strings Are Anagrams (Without Using Sorting)

Problem:
Write a function to check if two strings are anagrams of each other using only dictionary counting.

Sample Input: "silent", "listen"
Expected Output: True
'''

def isAnagram(str1, str2):
  if len(str1) != len(str2):
    return False
  else:
    str1_dict = {}
    str2_dict = {}
    for ch in str1:
      str1_dict[ch] = str1_dict.get(ch, 0) + 1
    for ch in str2:
      str2_dict[ch] = str2_dict.get(ch, 0) + 1
    return str1_dict == str2_dict

str1 = input('Enter First String: ')
str2 = input('Enter Second String: ')

print(isAnagram(str1, str2))
