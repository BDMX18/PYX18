'''
Palindrome Check (File):
Write a program to read each line from a text file and print only those lines which are palindromes.
'''

FO = open('text.txt', 'w')
FO.writelines(['madam ', 'hello ', 'level ', 'world ', 'racecar '])
FO.close()

palindrome = []
F = open('text.txt', 'r')
data = F.read()
data_list = data.split()
for word in data_list:
  if word == word[::-1]:
    palindrome.append(word)

print(palindrome)
