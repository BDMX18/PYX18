'''
5. Concatenate All Strings

Question: Given a list of strings, use reduce() to concatenate them into a single string with spaces.

Sample Data:
["Python", "is", "fun"]
Expected Output: "Python is fun"
'''

from functools import reduce as r

print(r(lambda str1, str2: str1+" "+str2, ["Python", "is", "fun"]))