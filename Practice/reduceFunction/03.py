'''
3. Longest Word in a List

Question: Given a list of strings, use reduce() to find the longest word.

Sample Data:
["apple", "banana", "grape", "watermelon"]
Expected Output: "watermelon"
'''

from functools import reduce as r
print(r(lambda a, b: a if len(a) > len(b) else b, ["apple", "banana", "grape", "watermelon"]))