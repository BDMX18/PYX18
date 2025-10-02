'''
Q2. Filter Palindromes from a List

Problem:
Write a Python function to filter out only palindromic strings from a list using filter and lambda.
Do not use loops.

Sample Input:

words = ["madam", "racecar", "python", "java", "level"]


Expected Output:

["madam", "racecar", "level"]
'''

words = ["madam", "racecar", "python", "java", "level"]

result = list(filter(lambda word: word == word[::-1], words))

print(result)