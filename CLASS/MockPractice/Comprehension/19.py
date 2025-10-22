'''
Question 4:
Given a list of strings, generate a list of all uppercase characters that appear in each string.

words = ["Hello", "Python", "WORLD", "Data"]
'''

words = ["Hello", "Python", "WORLD", "Data"]

op_list = [ch for word in words for ch in word if ch.isupper()]

print(op_list)