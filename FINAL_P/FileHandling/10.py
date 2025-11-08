'''
Q10. Count Number of Vowels and Consonants

Problem Statement:
Write a program that reads a text file and counts the total number of vowels and consonants in it.

Sample File (alphabets.txt):

Python programming is exciting and powerful.
'''

with open('alphabets.txt', 'w') as FO:
  FO.write('Python programming is exciting and powerful.')

with open('alphabets.txt', 'r') as FO:
  data = FO.read()

vowel_count = 0
consonant_count = 0

for char in data:
  if char.isalpha():
    if char.lower() in 'aeiou':
      vowel_count += 1
    else:
      consonant_count += 1

print('Vowels:', vowel_count, 'Consonants:', consonant_count)
