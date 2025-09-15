'''
8. Filter dictionary to include only items where the key is in a given list

Question:
Given a dictionary and a list of allowed keys, return only the entries where the key is in that list.

Sample Data:
'''

settings = {
    "theme": "dark",
    "language": "en",
    "notifications": True,
    "volume": 70,
    "timezone": "UTC"
}

allowed_keys = ["theme", "language", "timezone"]

print(dict(filter(lambda item: item[0] in allowed_keys, settings.items())))