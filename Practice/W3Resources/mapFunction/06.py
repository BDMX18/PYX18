'''
6. Case Conversion & Dedup Map

Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.

Original Characters:
 {'f', 'b', 'U', 'i', 'o', 'E', 'a'}

After converting above characters in upper and lower cases
and eliminating duplicate letters:
{('U', 'u'), ('O', 'o'), ('A', 'a'), ('B', 'b'), ('F', 'f'), ('I', 'i'), ('E', 'e')}
'''

def upperLower(char):
  return char.upper(), char.lower()

print(set(map(upperLower,  {'f', 'b', 'U', 'i', 'o', 'E', 'a'})))