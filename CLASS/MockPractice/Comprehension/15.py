'''
Question 15:
From a list of words, create a set of the first letters of each word.

words = ["apple", "banana", "grape", "kiwi", "mango"]
'''

words = ["apple", "banana", "grape", "kiwi", "mango"]

op_set = {word[0] for word in words}

print(op_set)