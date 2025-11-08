'''
Q1. Count Lines, Words, and Characters

Problem Statement:
Write a Python program that reads a text file and counts the total number of lines, words, and characters in it.

Sample File (sample1.txt):

Python is a powerful language.
It is widely used for web development and data analysis.
File handling is an important concept in Python.
'''

with open('q1.txt', 'w') as FO:
  FO.write('''Python is a powerful language.
  It is widely used for web development and data analysis.
  File handling is an important concept in Python.''')

with open('q1.txt', 'r') as FO:
  data = FO.readlines()

print('Number Of Lines:', len(data))
sentance = ' '.join(data)
char_count = 0
print('Number Of Characters:', len(sentance))
words = sentance.split()
print('Number Of Words:', len(words))

  