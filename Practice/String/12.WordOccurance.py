# Count word occurrences in a sentence.
# Write a Python program to count the occurrences of each word in a given sentence.

string = input('Enter A Sentance: ')
stringList = string.split()
dict = {}
for element in stringList:
  if element in dict:
    dict[element] += 1
  else:
    dict[element] = 1
print(dict)