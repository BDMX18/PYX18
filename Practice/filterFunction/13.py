'''
2. Filter out keys that start with a vowel

Question:
Given a dictionary of word frequencies, return a dictionary excluding keys that start with a vowel.

Sample Data:
'''

word_counts = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 3,
    "umbrella": 2
}

print(dict(filter(lambda item: item[0][0] in 'aeiou', word_counts.items())))