'''
Q3. Find the Longest Word in a File

Problem Statement:
Write a program that reads a text file and prints the longest word in it.

Sample File (words.txt):

Artificial Intelligence is transforming industries.
Automation and MachineLearning are key technologies.
'''

data = '''Artificial Intelligence is transforming industries.
Automation and MachineLearning are key technologies.'''

with open('q3.txt', 'w') as FO:
  FO.write(data)

with open('q3.txt', 'r') as FO:
  data = FO.read()

word_list = data.split()

largest = word_list[0]
for word in word_list:
  if len(word) > len(largest):
    largest = word

print(f'The Largest Word In The File, {largest} and it\'s Length Is {len(largest)}')