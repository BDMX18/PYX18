'''
Write a program to count the number of words, lines, and characters in a given text file.
'''

with open('demo.txt', 'w') as file:
  file.write('This is bibhu dutta mahapatra\n whos ijjbc nbjjwqb')

with open('demo.txt', 'r') as file:
  lines = file.readlines()
  line_count = 0
  for line in lines:
    line_count += 1
  # print(file.tell())
  file.seek(0)
  char = file.read()
  char_count = 0
  for ch in char:
    char_count += 1   
  print('Line Count:', line_count)
  print('Character Count:', char_count)
