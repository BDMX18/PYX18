'''
Q6. Search for a Word in a File

Problem Statement:
Write a program that takes a word as input and searches for it in a given text file.
Display the line numbers where the word occurs.

Sample File (story.txt):

Once upon a time, there was a brave knight.
The knight fought many battles.
Everyone admired the knight’s courage.
'''

data = ''' Once upon a time, there was a brave knight.
The knight fought many battles.
Everyone admired the knight’s courage.'''

with open('story.txt', 'w') as FO:
  FO.write(data)

word = input('Enter The Word You Want To Search In The File: ')
found = False

with open('story.txt', 'r') as FO:
  line_number = 1
  while True:
    line = FO.readline()
    if not line:
      break
    word_list = line.split()
    if word in word_list:
      print(f'The Given Word: {word} is in {line_number} number line')
      found = True
    line_number += 1

if not found:
  print(f'The given word: {word} is not found!')
