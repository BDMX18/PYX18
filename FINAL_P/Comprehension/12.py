'''
Q1. Index-Value Pair Transformation

Problem:
Given a list of strings, create a dictionary using dictionary comprehension where the key is the index of each element and the value is the string in uppercase.
Use enumerate().

Sample Data:

words = ['python', 'java', 'c++', 'go']


Expected Output:

{0: 'PYTHON', 1: 'JAVA', 2: 'C++', 3: 'GO'}
'''

words = ['python', 'java', 'c++', 'go']

op_dict = {i:words[i].upper() for i in range(len(words))}

print(op_dict)

op_dict_1 = {i:word.upper() for i, word in enumerate(words)}

print(op_dict_1)