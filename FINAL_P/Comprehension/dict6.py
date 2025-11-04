'''
Given a string, create a dictionary where key = character and value = ASCII value using dictionary comprehension.

text = "ABC"
# Expected Output: {'A': 65, 'B': 66, 'C': 67}
'''

text = 'ABC'

ascii_dict = {ch: ord(ch) for ch in text}

print(ascii_dict)