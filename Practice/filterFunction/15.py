'''
4. Filter dictionary to keep only keys with more than 5 characters

Question:
Given a dictionary of names and ages, return only the entries where the key (name) has more than 5 characters.
'''

ages = {
    "Alice": 25,
    "Bob": 30,
    "Charlotte": 22,
    "Daniel": 27,
    "Eve": 24
}

print(dict(filter(lambda item: len(item[0]) > 5, ages.items())))