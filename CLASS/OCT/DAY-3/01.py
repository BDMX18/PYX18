'''
1. Reverse Words in a String

Problem:
Write a function that takes a string of words separated by spaces and returns the string with the order of words reversed, but letters within words remain in the same order.

Example:
Input: "Hello World from Python"
Output: "Python from World Hello"
'''

def reverse(string):
  str_list = string.split()
  reverse_str = ''
  for word in str_list:
    reverse_str = word + ' ' + reverse_str
  return reverse_str

print(reverse('Hello World from Python'))