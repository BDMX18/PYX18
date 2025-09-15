'''
Filter strings that start with a vowel.
From a list of strings, return only those that start with a vowel (a, e, i, o, u).
'''

words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi", "avocado"]

print(list(filter(lambda str: str[0] in 'aeiou', words)))