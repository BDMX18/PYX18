'''
Word Frequency Counter using map, reduce, and lambda

Problem:
Write a Python program that counts the frequency of words in a given string using functional programming. You must avoid explicit loops.

Sample Input:

text = "the quick brown fox jumps over the lazy dog the quick fox"


Expected Output:

{'the': 3, 'quick': 2, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
'''

from functools import reduce

text = "the quick brown fox jumps over the lazy dog the quick fox"

word_list = text.split()

word_count = reduce(lambda acc, word: (acc.update({word: acc.get(word, 0)+1})) or acc, word_list, {})

print(word_count)