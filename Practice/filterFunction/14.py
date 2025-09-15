'''
3. Filter dictionary to keep entries with even integer values

Question:
Given a dictionary of scores, return only the entries where the score is an even number.

Sample Data:
'''

scores = {
    "Alice": 45,
    "Bob": 62,
    "Charlie": 73,
    "Daisy": 80,
    "Eve": 91
}

print(dict(filter(lambda item: item[1]%2==0, scores.items())))