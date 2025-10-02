'''
Word Length Mapping
From a list of words, build a dict mapping each word to its length.

Input: ["apple", "banana", "cherry"]  
Output: {"apple": 5, "banana": 6, "cherry": 6}
'''
words = ["apple", "banana", "cherry"]  

length_dict = {word: len(word) for word in words}

print(length_dict)