'''
Q9. Merge Two Files into a Third File

Problem Statement:
Write a Python program that merges the contents of two text files into a third file.

Sample Files:

part1.txt

Python is an interpreted language.


part2.txt

It is dynamically typed and easy to learn.
'''

part1 = 'Python is an interpreted language.'
part2 = 'It is dynamically typed and easy to learn.'

with open('part1.txt', 'w+') as FO:
  FO.write(part1)
  FO.seek(0)
  part1_data = FO.read()

with open('part2.txt', 'w+') as FO:
  FO.write(part2)
  FO.seek(0)
  part2_data = FO.read()

with open('part3.txt', 'w+') as FO:
  FO.write(part1_data +' '+ part2_data)
  FO.seek(0)
  data = FO.read()
  print(data)

