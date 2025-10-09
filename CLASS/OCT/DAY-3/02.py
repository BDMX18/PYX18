'''
2. Check for Palindrome Ignoring Non-Alphanumeric Characters

Problem:
Write a function that checks if a given string is a palindrome. Ignore spaces, punctuation, and case.

Example:
Input: "A man, a plan, a canal: Panama"
Output: True

Input: "Hello"
Output: False
'''

def isPalindrome(string):
  dummy = ''
  new_str = ''
  for letter in string:
    if letter.isalpha():
      dummy += letter.lower()
      new_str = letter.lower()  + new_str
  if dummy == new_str:
    return True
  else:
    return False

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome('Hello'))