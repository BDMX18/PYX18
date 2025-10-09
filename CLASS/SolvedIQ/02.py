# 2. Write a program to delete all consonants from the given string: 'Python and Data Science'.

str = 'Python and Data Science 123'
new_str = ''
for ch in str:
    if ch in 'aeiouAEIOU' or not ch.isalpha():
      new_str += ch
print(new_str)
