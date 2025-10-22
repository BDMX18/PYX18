'''
Question 2:
From a list of strings, create a list containing only strings that start with a vowel.
'''

words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]

vowel = [word for word in words if word[0].lower() in 'aeiou']

print(vowel)