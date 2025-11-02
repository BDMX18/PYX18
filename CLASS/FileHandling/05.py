'''
Read Entire File Content

Question:
Write a program to open sample1.txt and display its entire content on the console.

Sample File (sample1.txt):
'''

FO = open('sample1.txt', 'r')
data = FO.read()
print(data)