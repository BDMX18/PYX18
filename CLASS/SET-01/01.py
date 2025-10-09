#  1. Write a function to reverse a string without using slicing.

def reverse_string(string):
  reverse = ''
  for ch in string:
    reverse  = ch + reverse
  return reverse

print(reverse_string('Python'))