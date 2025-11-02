'''
Count Digits and Alphabets:
Write a program to count the number of digits and alphabets in a given string.
'''

text = 'Hello123World45'
digit_count = 0
alpha_count = 0
for ch in text:
  if ch.isalpha():
    alpha_count += 1
  elif ch.isdigit():
    digit_count += 1
print(f'Alphabet Count: {alpha_count} \nDigit Count: {digit_count}')

