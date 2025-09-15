'''
Filter words longer than 5 characters.
Given a list of strings, return only the words whose length is greater than 5.
'''

print(list(filter(lambda string: len(string) > 5, ["apple", "banana", "grape", "watermelon", "fig", "strawberry"])))
