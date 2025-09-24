'''
7. map() Interview Question

Q: Given a list of strings, write a program to return a list of lengths of each string using map().

words = ["apple", "banana", "cherry", "date"]
'''

words = ["apple", "banana", "cherry", "date"]

print(list(map(lambda item:len(item), words)))