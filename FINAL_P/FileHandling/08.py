'''
Q8. Count Frequency of Each Word

Problem Statement:
Write a Python program to count the frequency of each word in a text file and display the result in descending order of frequency.

Sample File (data.txt):

Python Python Java C++ Python Java
C C++ JavaScript Java Python
'''

data = '''Python Python Java C++ Python Java
C C++ JavaScript Java Python'''

with open('data.txt', 'w') as FO:
  FO.write(data)

with open('data.txt', 'r') as FO:
  data = FO.read()

data_split = data.split()

occurance_dict = {}
for word in data_split:
  if word not in occurance_dict:
    occurance_dict[word] = 1
  else:
    occurance_dict[word] += 1

print(occurance_dict)