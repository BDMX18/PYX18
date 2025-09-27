'''
Create a list of the lengths of each word in a given list of words using list comprehension.
'''

words = ['hello', 'world', 'python', 'is', 'awesome']

words = [len(item) for item in words]
print(words)