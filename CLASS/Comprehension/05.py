'''
Use list comprehension to extract all words longer than 3 characters from a given sentence.
'''

sentence = "Python is an amazing language to learn"

op_list = [word for word in sentence.split() if len(word) > 3]

print(op_list)