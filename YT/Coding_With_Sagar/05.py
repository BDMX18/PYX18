'''
Reverse each word in a sentance
Write a program to reverse each word in the sentance 'Hello World' using a while loop
Expected Output: olleH dlroW
'''

sentance = input('Enter A Sentance: ')
words = sentance.split()
reverse_sentance = ''
for word in words:
  ip = -1
  reverse = ''
  while ip >= -(len(word)):
    reverse += word[ip]
    ip -= 1
  reverse_sentance += reverse + ' '
print(reverse_sentance)
