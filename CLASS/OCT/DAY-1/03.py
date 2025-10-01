'''
Question: Functional Palindrome Filter

Write a Python function called filter_palindromes(words) that:

Takes a list of strings called words as input.

Uses functional programming tools (map, filter, lambda, etc.) to:

Convert all words to lowercase.

Filter out all words that are not palindromes (words that read the same backward and forward).

Returns a list of palindromes in lowercase.

Example:
input_words = ['Level', 'World', 'radar', 'Python', 'madam', 'ChatGPT']

print(filter_palindromes(input_words))


Expected output:

['level', 'radar', 'madam']
'''

def isPalindrome(word):
  dummy = word
  if (dummy[::-1] == word):
    return True
  else:
    return False

def inputWords(num):
  word_list = []
  for i in range(num):
    word = input(f'Enter Word {i+1}: ')
    word_list.append(word)
  palindrome_list = []
  for word in word_list:
    word = word.lower()
    if isPalindrome(word):
      palindrome_list.append(word)
  return palindrome_list

num = int(input('Enter The Number Of Words: '))
print(inputWords(num))