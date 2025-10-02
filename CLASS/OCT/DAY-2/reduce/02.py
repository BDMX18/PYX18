'''
Find the Longest Word

Problem:
Given a list of words, use reduce to find the longest word.

Sample Input:

words = ["python", "java", "javascript", "c", "golang"]


Expected Output:

"javascript"
'''

from functools import reduce as r

words = ["python", "java", "javascript", "c", "golang"]

result = r(lambda a, b: a if len(a)>len(b) else b, words)

print('Longest Word:', result)