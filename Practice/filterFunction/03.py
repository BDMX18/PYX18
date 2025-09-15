'''
Filter palindromes.
From a list of strings, return only the words that are palindromes.
'''

def palindrome_str(string):
  reverse = ''
  for ch in string:
    reverse = ch + reverse
  if reverse == string:
    return True
  else:
    return False

print(list(filter(palindrome_str, ["madam", "racecar", "apple", "level", "world", "noon"])))