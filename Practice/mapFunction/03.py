'''
Uppercase All Strings:
Use map() to convert a list of lowercase words to uppercase.
Example input: ["apple", "banana", "grape"] → Output: ["APPLE", "BANANA", "GRAPE"]
'''

def uppercase(str):
  return str.upper()

print(list(map(uppercase, ["apple", "banana", "grape"])))

print(list(map(lambda word: word.upper(), ["apple", "banana", "grape"])))
