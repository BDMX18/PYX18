'''
Question 12:
From a list of words, create a set containing only the words with length > 4.

words = ["apple", "bat", "carrot", "dog", "elephant"]
'''


words = ["apple", "bat", "carrot", "dog", "elephant"]

op_set = {word for word in words if len(word) > 4}

print(op_set)