'''
Question 11:
From a list of words, create a set of all unique vowels in words longer than 4 characters.

words = ["apple", "bat", "carrot", "dog", "elephant"]
'''

words = ["apple", "bat", "carrot", "dog", "elephant"]

op_set = {ch for word in words for ch in word if len(word) > 4 and ch.lower() in 'aeiou'}

print(op_set)