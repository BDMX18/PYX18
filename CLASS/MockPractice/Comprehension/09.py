'''
Question 9:
Convert a list of strings into a dictionary where key = string and value = length of string.

words = ["apple", "banana", "kiwi", "grape"]
'''


words = ["apple", "banana", "kiwi", "grape"]

op_dict = {word: len(word) for word in words}

print(op_dict)