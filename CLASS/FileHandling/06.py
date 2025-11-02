'''
Count Lines, Words, and Characters

Question:
Write a program to count how many lines, words, and characters are present in sample2.txt.
'''

with open('sample1.txt', 'r') as FO:
  data = FO.read()
  line = FO.readlines()

word_count = 0
char_count = 0
word_list = data.split()
for word in word_list:
  word_count += 1
for ch in data:
  char_count += 1
print(f'Word Count: {word_count}, Character Count: {char_count}, Line Count: {len(line)}')

