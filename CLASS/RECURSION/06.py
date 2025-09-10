# Write a recursive function to check if a string is a palindrome.

def palindrome(string):
  if len(string) == 0:
    return ''
  return string[-1] + palindrome(string[1:])

print(palindrome('bibhu'))