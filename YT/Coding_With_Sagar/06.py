'''
Count Consonants in a string
Write a program to count the number of consonants in the word 'Learning'.
Input: Learning
Expected Output: 5
'''

string = input('Enter A String: ')
count = 0
ip = 0
while ip < len(string):
  if(string[ip] not in 'aeiouAEIOU'):
    count += 1
  ip += 1
print(count)