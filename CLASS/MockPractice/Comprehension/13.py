'''
Question 13:
Create a set of all vowels present in a given string.

sentence = "Python is an amazing language"
'''

sentence = "Python is an amazing language"

op_set = {ch for ch in sentence if ch.lower() in 'aeiou'}

print(op_set)