'''
Use list comprehension to convert all strings in a list to uppercase.
'''

words = ['apple', 'banana', 'cherry', 'date']

words = [item.upper() for item in words]
print(words)