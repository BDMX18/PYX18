'''
Count Vowels and Consonants:
Count how many vowels and consonants are present in a given string.
'''

ip_str = input('Enter a string: ')
vowel_count = 0
consonant_count = 0
for ch in ip_str:
  if ch.lower() in 'aeiou':
    vowel_count += 1
  else:
    consonant_count += 1
print(f'Vowel Count: {vowel_count}\nConsonant Count: {consonant_count}')