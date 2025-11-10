'''
Q1. Merge and Sort Data from Multiple Files

Problem Statement:
You are given multiple text files, each containing a list of numbers (one per line).
Write a Python program that merges the contents of all these files into a single file named merged.txt, removes duplicates, and sorts the numbers in ascending order.

Sample Files:

file1.txt → 
12
7
5
9

file2.txt → 
9
4
7
10


Expected Output (merged.txt):

4
5
7
9
10
12
'''

data_1 = ['12\n', '7\n', '5\n', '9\n']
data_2 = ['9\n', '4\n', '7\n', '10\n']

with open('file_1.txt', 'w+') as FO:
  FO.writelines(data_1)
  FO.seek(0)
  file_1_data = FO.read()

with open('file_2.txt', 'w+') as FO:
  FO.writelines(data_2)
  FO.seek(0)
  file_2_data = FO.read()

with open('merged.txt', 'w+') as FO:
  merge = file_1_data + file_2_data
  for data in merge:
    if data not in FO:
      FO.write(data)
  FO.seek(0)
  merge_data = FO.read()

print(merge_data)


