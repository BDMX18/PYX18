'''
Count Occurrences of a Character in a String
Write a recursive function to count how many times a given character appears in a string.
'''

def occurance(string, char):
  if not string:
    return 0
  count = 1 if string[0] == char else 0
  return count + occurance(string[1:], char)

string = input('Enter A String: ')
char = input('Enter A Character: ')
print(occurance(string, char))