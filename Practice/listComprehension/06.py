'''
Given a list of strings, use list comprehension to create a new list that contains only those strings that start with the letter ‘a’.
'''

words = ['apple', 'banana', 'avocado', 'cherry', 'apricot', 'blueberry']

words = [item for item in words if item.startswith('a')]
print(words)

word = [item for item in words if item[0] == 'a']
print(word)