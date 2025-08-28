'''
2. Add Key to Dictionary
Write a Python script to add a key to a dictionary.
  Sample Dictionary : {0: 10, 1: 20}
  Expected Result : {0: 10, 1: 20, 2: 30}
'''

Dictionary = {0: 10, 1: 20}

# Approach 01:
Dictionary[3] = 30

# Approach 02: Herein, we'll be using dictionary built-in method, update() to add element to the dictionary.

# With this method, we can pass data in the form of pairs (i.e: Key-Value) defined within list, set or tuple.
Dictionary.update({3:30})

# Approach 03:
Dictionary.update([[3, 30]])

print(Dictionary)