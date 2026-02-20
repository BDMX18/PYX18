'''
Q1. Write a program to merge the contents of two files into a third file without duplicates.

Sample:
File1 → ["apple", "banana", "orange"]
File2 → ["banana", "grapes", "apple"]

Create: File3 → only unique values.
'''

File1 = ["apple\n", "banana\n", "orange\n"]
File2 = ["banana\n", "grapes\n", "apple\n"]

with open('fileOne.txt', 'w') as FO1:
  FO1.writelines(File1)

with open('fileTwo.txt', 'w') as FO2:
  FO2.writelines(File2)

with open('fileOne.txt', 'r') as FO1, open('fileTwo.txt', 'r') as FO2:
  data1 = FO1.readlines()
  print(data1)
  data2 = FO2.readlines()

with open('MergeFile.txt', 'w') as MF:
  merge_data = set(data1+data2)
  MF.writelines(merge_data)